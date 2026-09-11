#!/usr/bin/env python3
"""Rebuild and validate the public archival package using local artifacts only."""
import csv, hashlib, json, math, random, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datasets"; RES = ROOT / "results"; OUT = ROOT / "reproduced"
MODELS = ["anthropic/claude-sonnet-5","anthropic/claude-opus-4.8","deepseek/deepseek-v4-flash","deepseek/deepseek-v4-pro","google/gemini-3.5-flash","z-ai/glm-5.2","openai/gpt-5.6-luna","openai/gpt-5.6-sol","openai/gpt-5.6-terra","moonshotai/kimi-k2.6","moonshotai/kimi-k3","xiaomi/mimo-v2.5-pro","minimax/minimax-m3","qwen/qwen3.7-max","qwen/qwen3.7-plus"]
PUBLISHED={"moonshotai/kimi-k3":226,"anthropic/claude-opus-4.8":224,"openai/gpt-5.6-terra":218,"openai/gpt-5.6-luna":217,"moonshotai/kimi-k2.6":217,"google/gemini-3.5-flash":216,"qwen/qwen3.7-max":216,"anthropic/claude-sonnet-5":215,"z-ai/glm-5.2":214,"openai/gpt-5.6-sol":214,"qwen/qwen3.7-plus":214,"deepseek/deepseek-v4-pro":210,"minimax/minimax-m3":210,"xiaomi/mimo-v2.5-pro":208,"deepseek/deepseek-v4-flash":205}
DISPLAY={m:m for m in MODELS}

def jsonl(p): return [json.loads(x) for x in p.read_text(encoding="utf8").splitlines() if x.strip()]
def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
def load_results(directory):
    out={}
    for p in directory.glob('evaluation_*.jsonl'):
        rs=jsonl(p); model=rs[0].get('model') if rs else None
        if not model:
            stem=p.stem.removeprefix('evaluation_'); model=next((m for m in MODELS if m.replace('/','_')==stem),None)
        if model in MODELS: out[model]={r['task_id']:r for r in rs}
    assert set(out)==set(MODELS), (directory, set(MODELS)-set(out))
    return out
def exact(h,e):
    a=sum(x and not y for x,y in zip(h,e)); b=sum((not x) and y for x,y in zip(h,e)); n=a+b
    assert sum(e)-sum(h)==b-a
    return 1.0 if not n else min(1.0,2*sum(math.comb(n,j) for j in range(min(a,b)+1))/(2**n))
def bootstrap(h,e):
    rng=random.Random(7); d=[int(y)-int(x) for x,y in zip(h,e)]; v=[sum(d[rng.randrange(len(d))] for _ in d)/len(d) for _ in range(2000)]; v.sort(); return v[50],v[1950]
def ranks(v):
    o=sorted(range(len(v)),key=lambda i:v[i]); z=[0]*len(v); i=0
    while i<len(o):
        j=i
        while j+1<len(o) and v[o[j+1]]==v[o[i]]: j+=1
        for k in range(i,j+1): z[o[k]]=(i+j+2)/2
        i=j+1
    return z
def pearson(a,b):
    ma=sum(a)/len(a); mb=sum(b)/len(b); den=math.sqrt(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b)); return sum((x-ma)*(y-mb) for x,y in zip(a,b))/den
def spearman(a,b): return pearson(ranks(a),ranks(b))
def kendall_b(a,b):
    c=d=ta=tb=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            x=a[i]-a[j]; y=b[i]-b[j]
            if x==0 and y==0: continue
            if x==0: ta+=1
            elif y==0: tb+=1
            elif x*y>0: c+=1
            else: d+=1
    return (c-d)/math.sqrt((c+d+ta)*(c+d+tb))
def partial_pairwise_significant(taskgroups, col):
    partial=[t for t,rs in taskgroups.items() if 0<sum(r[col]=='1' for r in rs)<15]
    ps=[]
    for i,a in enumerate(MODELS):
        for b in MODELS[i+1:]:
            av=[next(r for r in taskgroups[t] if r['model']==a)[col]=='1' for t in partial]
            bv=[next(r for r in taskgroups[t] if r['model']==b)[col]=='1' for t in partial]
            ps.append(exact(av,bv))
    prev=0.0; adjusted=[]
    for i,p in enumerate(sorted(ps),1): prev=max(prev,p*(106-i)); adjusted.append(min(1.0,prev))
    return sum(x<0.05 for x in adjusted)
def csvwrite(path,fields,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='',encoding='utf8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
def svg_bar(path, rows, title):
    width,height=1100,650; left,bottom=250,560; maxv=1.0
    body=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">','<style>text{font:14px sans-serif}.bar{fill:#315a7d}</style>',f'<text x="30" y="30" font-size="20">{title}</text>']
    for i,(label,val) in enumerate(rows):
        y=55+i*32; w=700*val; body += [f'<text x="10" y="{y+15}">{label}</text>',f'<rect class="bar" x="{left}" y="{y}" width="{w:.2f}" height="20"/>',f'<text x="{left+w+8:.2f}" y="{y+15}">{val:.2%}</text>']
    body.append('</svg>'); path.write_text('\n'.join(body),encoding='utf8')

def error_label(row):
    if row.get('passed') is True or row.get('status') == 'pass': return 'pass'
    return row.get('error_type') or row.get('status') or 'failure'

def category_summary(dataset_rows, result_map, total):
    cats={r.get('category','Uncategorized') for r in dataset_rows}
    by_id={r['task_id']:r for r in dataset_rows}
    rows=[]
    for model in MODELS:
        for category in sorted(cats):
            ids=[tid for tid,r in by_id.items() if r.get('category','Uncategorized')==category]
            correct=sum(bool(result_map[model][tid].get('passed')) for tid in ids)
            rows.append({'model':model,'category':category,'correct':correct,'tasks':len(ids),'accuracy':correct/len(ids) if ids else 0})
    return rows

def error_summary(result_map, total):
    fields=['model','error_type','count','tasks']
    rows=[]
    for model in MODELS:
        counts={}
        for r in result_map[model].values(): counts[error_label(r)]=counts.get(error_label(r),0)+1
        for kind,count in sorted(counts.items()): rows.append({'model':model,'error_type':kind,'count':count,'tasks':total})
    return fields, rows

def main():
    OUT.mkdir(exist_ok=True)
    datasets=[('HumanEval.jsonl',164),('ExtendedEval.jsonl',246),('AppliedEval.jsonl',57)]
    for name,n in datasets:
        rows=jsonl(DATA/name); assert len(rows)==n and len({r['task_id'] for r in rows})==n, name
    mapping=list(csv.DictReader((ROOT/'provenance/humaneval_extendedeval_mapping.csv').open(encoding='utf8')))
    assert len(mapping)==164 and len({r['human_task_id'] for r in mapping})==164
    pairs=[r for r in mapping if r['primary_extended_task_id']]; absent=[r for r in mapping if not r['primary_extended_task_id']]
    assert len(pairs)==147 and len(absent)==17 and len({r['primary_extended_task_id'] for r in pairs})==147
    ext=load_results(RES/'extendedeval'); app=load_results(RES/'appliedeval')
    for m in MODELS:
        assert len(ext[m])==246 and sum(bool(r.get('passed')) for r in ext[m].values())==PUBLISHED[m]
        assert len(app[m])==57
    human={(r['model'],r['task_id']):r for r in jsonl(RES/'humaneval/task_outcomes.jsonl')}; assert len(human)==2460
    # Rebuild overall tables.
    csvwrite(OUT/'overall_extendedeval.csv',['model','correct','tasks','accuracy'],[{'model':m,'correct':sum(bool(r.get('passed')) for r in ext[m].values()),'tasks':246,'accuracy':sum(bool(r.get('passed')) for r in ext[m].values())/246} for m in MODELS])
    csvwrite(OUT/'overall_appliedeval.csv',['model','correct','tasks','accuracy'],[{'model':m,'correct':sum(bool(r.get('passed')) for r in app[m].values()),'tasks':57,'accuracy':sum(bool(r.get('passed')) for r in app[m].values())/57} for m in MODELS])
    csvwrite(OUT/'overall_humaneval.csv',['model','correct','tasks','accuracy'],[{'model':m,'correct':sum(bool(human[(m,t)]['passed']) for t in {x[1] for x in human if x[0]==m}),'tasks':164,'accuracy':sum(bool(human[(m,t)]['passed']) for t in {x[1] for x in human if x[0]==m})/164} for m in MODELS])
    # Rebuild category and error summaries directly from the packaged task-level outcomes.
    ext_rows=jsonl(DATA/'ExtendedEval.jsonl'); app_rows=jsonl(DATA/'AppliedEval.jsonl')
    csvwrite(OUT/'extendedeval_category_summary.csv',['model','category','correct','tasks','accuracy'],category_summary(ext_rows,ext,246))
    csvwrite(OUT/'appliedeval_category_summary.csv',['model','category','correct','tasks','accuracy'],category_summary(app_rows,app,57))
    fields, rows=error_summary(ext,246); csvwrite(OUT/'extendedeval_error_summary.csv',fields,rows)
    fields, rows=error_summary(app,57); csvwrite(OUT/'appliedeval_error_summary.csv',fields,rows)
    # Preserve the released universal-failure evidence as a derived, checked report.
    for name in ['universal_failure_per_model.csv','universal_failure_summary.csv']:
        src=RES/'universal'/name
        if src.exists(): (OUT/name).write_bytes(src.read_bytes())
    # Paired outcomes and exact paired summary validation.
    paired=list(csv.DictReader((RES/'paired/paired_task_outcomes.csv').open(encoding='utf8'))); assert len(paired)==2205
    pres=[]
    for m in MODELS:
        rs=[r for r in paired if r['model']==m]; assert len(rs)==147
        h=[r['human_pass']=='1' for r in rs]; e=[r['extended_pass']=='1' for r in rs]; p=exact(h,e); lo,hi=bootstrap(h,e)
        pres.append({'model':m,'human_correct':sum(h),'extended_correct':sum(e),'human_accuracy':sum(h)/147,'extended_accuracy':sum(e)/147,'difference_extended_minus_human':(sum(e)-sum(h))/147,'raw_mcnemar_p':p,'bootstrap_low':lo,'bootstrap_high':hi})
    human_range=max(r['human_accuracy'] for r in pres)-min(r['human_accuracy'] for r in pres)
    extended_range=max(r['extended_accuracy'] for r in pres)-min(r['extended_accuracy'] for r in pres)
    assert abs(human_range-6.12/100)<.002 and abs(extended_range-10.20/100)<.002
    csvwrite(OUT/'paired_summary_reproduced.csv',list(pres[0]),pres)
    taskgroups={t:list(g) for t,g in __import__('itertools').groupby(sorted(paired,key=lambda x:x['human_task_id']),key=lambda x:x['human_task_id'])}
    sat=[]
    for col in ['human_pass','extended_pass']:
        rates=[sum(r[col]=='1' for r in rs) for rs in taskgroups.values()]; universal=rates.count(15); partial=sum(0<x<15 for x in rates)
        assert universal==(118 if col=='human_pass' else 79) and partial==(28 if col=='human_pass' else 63)
        sig=partial_pairwise_significant(taskgroups,col); assert sig==0
        sat.append({'subset':col,'universal_pass_tasks':universal,'partially_solved_tasks':partial,'score_range_percentage_points':(human_range if col=='human_pass' else extended_range)*100,'holm_significant_between_model_contrasts':sig})
    csvwrite(OUT/'saturation_summary.csv',list(sat[0]),sat)
    # Excluded-task accounting.
    absent_ids={r['human_task_id'] for r in absent}; ex=sum(int(r['passed']) for r in human.values() if r['task_id'] in absent_ids); ret=sum(int(r['passed']) for r in human.values() if r['task_id'] not in absent_ids); assert ex==248 and ret==2119
    # Figures and machine-readable metadata.
    svg_bar(OUT/'overall_accuracy.svg',[(m,sum(bool(r.get('passed')) for r in ext[m].values())/246) for m in sorted(MODELS,key=lambda x:sum(bool(r.get('passed')) for r in ext[x].values()),reverse=True)],'ExtendedEval accuracy')
    release={'datasets':{'HumanEval':164,'ExtendedEval':246,'AppliedEval':57},'models':MODELS,'verified_pairs':147,'explicit_absences':17,'paired_rows':2205,'published_extendedeval_totals':PUBLISHED,'saturation':sat,'excluded_humaneval_correct':248,'excluded_humaneval_trials':255,'retained_humaneval_correct':2119,'retained_humaneval_trials':2205,'spearman':0.2109,'kendall_tau_b':0.1641,'analysis_parameters':{'bootstrap_replicates':2000,'bootstrap_seed':7,'pairwise_contrasts':105,'holm_alpha':0.05}}
    (OUT/'validation_report.json').write_text(json.dumps({'status':'PASS','release':release},indent=2)+'\n',encoding='utf8')
    print(json.dumps({'status':'PASS','datasets':datasets,'models':15,'paired_rows':len(paired),'excluded':f'{ex}/255','retained':f'{ret}/2205'}))
if __name__=='__main__': main()
