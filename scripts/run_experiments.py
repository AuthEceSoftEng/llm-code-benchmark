#!/usr/bin/env python3
"""Re-run completions through OpenRouter using only public package inputs.

This script never contains credentials. Set OPENROUTER_API_KEY in the shell.
It records the raw provider JSON, extracted text, configuration, retries, and
timestamps. Existing successful records are reused only when --resume is set.
"""
import argparse, json, os, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

NO_THINKING = "\n\nReturn only the final answer/code needed to solve the task. Do not show chain-of-thought or hidden reasoning."

def post(url, body, key, timeout):
    req=Request(url, data=json.dumps(body).encode(), headers={"Authorization":f"Bearer {key}","Content-Type":"application/json","HTTP-Referer":"https://github.com/AuthEceSoftEng/llm-code-benchmark","X-Title":"LLM Code Benchmark"}, method="POST")
    with urlopen(req, timeout=timeout) as r: return json.loads(r.read())

def text(payload):
    choice=(payload.get("choices") or [{}])[0]; msg=choice.get("message") or {}
    value=msg.get("content", "")
    if isinstance(value, str): return value
    if isinstance(value, list): return "".join(str(x.get("text", "")) for x in value if isinstance(x, dict))
    return str(value)

def main():
    p=argparse.ArgumentParser(); p.add_argument("--dataset",required=True,type=Path); p.add_argument("--model",required=True); p.add_argument("--output",required=True,type=Path); p.add_argument("--field",default="prompt"); p.add_argument("--workers",type=int,default=50); p.add_argument("--max-tokens",type=int,default=16384); p.add_argument("--temperature",type=float,default=0); p.add_argument("--top-p",type=float,default=1); p.add_argument("--timeout",type=float,default=300); p.add_argument("--retries",type=int,default=2); p.add_argument("--limit",type=int); p.add_argument("--resume",action="store_true"); p.add_argument("--reasoning",choices=["none","minimal","allow"],default="none"); a=p.parse_args()
    key=os.environ.get("OPENROUTER_API_KEY")
    if not key: p.error("set OPENROUTER_API_KEY; no key is stored in this package")
    rows=[json.loads(x) for x in a.dataset.read_text(encoding="utf8").splitlines() if x.strip()]
    if a.limit is not None: rows=rows[:a.limit]
    existing={}
    if a.resume and a.output.exists():
        for line in a.output.read_text(encoding="utf8").splitlines():
            try:
                r=json.loads(line)
                if r.get("success"): existing[r.get("task_id")]=r
            except json.JSONDecodeError: pass
    pending=[(i,r) for i,r in enumerate(rows) if r.get("task_id") not in existing]
    reasoning=None if a.reasoning=="allow" else ({"effort":"none","exclude":True} if a.reasoning=="none" else {"effort":"low","exclude":True})
    def run(pair):
        i,r=pair; started=datetime.now(timezone.utc).isoformat(); attempts=[]; last=""
        for n in range(1,a.retries+2):
            try:
                body={"model":a.model,"messages":[{"role":"user","content":str(r[a.field])+NO_THINKING}],"temperature":a.temperature,"top_p":a.top_p,"max_tokens":a.max_tokens}
                if reasoning is not None: body["reasoning"]=reasoning; body["include_reasoning"]=False
                payload=post("https://openrouter.ai/api/v1/chat/completions",body,key,a.timeout)
                return {"task_id":r.get("task_id",f"index_{i}"),"dataset_index":i,"model":a.model,"success":True,"response":text(payload),"raw_provider_response":payload,"generation":body,"attempts":attempts+[{"attempt":n,"returned_completion":True}],"started_at":started,"finished_at":datetime.now(timezone.utc).isoformat()}
            except (HTTPError,URLError,TimeoutError,ValueError) as e:
                last=str(e); attempts.append({"attempt":n,"returned_completion":False,"error":last});
                if n<=a.retries: time.sleep(min(2**(n-1),15))
        return {"task_id":r.get("task_id",f"index_{i}"),"dataset_index":i,"model":a.model,"success":False,"error":last,"attempts":attempts,"started_at":started,"finished_at":datetime.now(timezone.utc).isoformat()}
    results=dict(existing)
    with ThreadPoolExecutor(max_workers=max(1,a.workers)) as ex:
        for f in as_completed([ex.submit(run,x) for x in pending]):
            r=f.result(); results[r["task_id"]]=r; print(("OK" if r["success"] else "ERROR"),r["task_id"],flush=True)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open("w",encoding="utf8") as f:
        for r in rows: f.write(json.dumps(results.get(r.get("task_id")),ensure_ascii=False)+"\n")
    print(f"Completed {len(rows)} tasks; successful: {sum(bool(results.get(r.get('task_id'),{}).get('success')) for r in rows)}; results saved to {a.output}")
if __name__=="__main__": main()
