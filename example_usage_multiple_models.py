#!/usr/bin/env python3
"""
Simple Multiple Models Testing Script (dataset-enabled)
======================================================
Tests multiple models from different providers (OpenAI, Claude, AWS Bedrock, Google, xAI Grok)
either with a single question or with many questions loaded from JSONL datasets.

Environment Variables:
You can either:
1. Create a .env file (copy from .env.example and fill in your keys)
2. Or export them in your shell:
   - OPENAI_API_KEY
   - CLAUDE_API_KEY (or ANTHROPIC_API_KEY)
   - AWS_ACCESS_KEY_ID / AWS_PROFILE
   - AWS_SECRET_ACCESS_KEY (if not using profile)
   - AWS_REGION (optional, defaults to us-east-1)
   - GOOGLE_API_KEY
   - XAI_API_KEY

Usage (single question):
    python example_usage_multiple_models.py --question "Explain AI"

Usage (dataset mode - one or more files):
    python example_usage_multiple_models.py --dataset final_custom_eval.jsonl MyOwnBench.jsonl

Choose the field that contains the prompt/question (default: "question"):
    python example_usage_multiple_models.py --dataset bench.jsonl --field input

Save outputs to a specific file:
    python example_usage_multiple_models.py --dataset bench.jsonl --out results.jsonl

Region override for Bedrock:
    python example_usage_multiple_models.py --region eu-central-1
"""

import asyncio
import os
import time
import json
import argparse
from datetime import datetime
from typing import List, Dict, Any, Iterable

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

from multi_llm_sdk import MultiLLM
from multi_llm_sdk.core.models import LLMConfig, Message

# ---------------------------
# Configuration
# ---------------------------
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
TEST_QUESTION = "Hello! Please explain what you are and briefly describe your capabilities."

# Model lists for each provider
OPENAI_MODELS = [
     "gpt-5-2025-08-07",
    # "gpt-5-mini"
]

GOOGLE_MODELS = [
     "gemini-2.5-pro",
    "gemini-2.5-flash",
    # "gemini-2.0-flash",
    # "gemini-1.5-pro",
    # "gemini-1.5-flash",
]

CLAUDE_MODELS = [
    # e.g. "claude-3-7-sonnet-2025-xx-xx"
]

BEDROCK_MODELS = [
     "us.anthropic.claude-3-5-haiku-20241022-v1:0",
     "us.anthropic.claude-sonnet-4-20250514-v1:0",
    # "us.anthropic.claude-opus-4-20250514-v1:0",
    # "us.meta.llama3-3-70b-instruct-v1:0",
    # "eu.mistral.pixtral-large-2502-v1:0",
]

GROK_MODELS = [
    "grok-4",
     "grok-code-fast-1",
]

# ---------------------------
# Utilities
# ---------------------------
def check_credentials():
    """Check which API credentials are available."""
    print("🔑 Checking API Credentials...")
    credentials = {
        "openai": bool(os.getenv("OPENAI_API_KEY")),
        "claude": bool(os.getenv("CLAUDE_API_KEY")),
        "bedrock": bool(os.getenv("AWS_ACCESS_KEY_ID")) or bool(os.getenv("AWS_PROFILE")),
        "google": bool(os.getenv("GOOGLE_API_KEY")),
        "grok": bool(os.getenv("XAI_API_KEY")),
    }

    for provider, available in credentials.items():
        status = "✅ Available" if available else "❌ Not set"
        print(f"   {provider.upper()}: {status}")

    if credentials["bedrock"]:
        print(f"   AWS Region: {AWS_REGION}")

    return credentials


def load_jsonl(path: str) -> Iterable[Any]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


def load_questions_from_datasets(paths: List[str], field: str) -> List[Dict[str, Any]]:
    """
    Returns a list of dicts:
    {
        "dataset_file": <filename>,
        "index": <0-based>,
        "question": <text>,
        "raw": <whole json object>
    }
    """
    items = []
    for p in paths:
        i = 0
        for obj in load_jsonl(p):
            q = None
            if isinstance(obj, dict) and field in obj:
                q = obj[field]
            elif isinstance(obj, dict):
                for alt in ("question", "prompt", "input", "query"):
                    if alt in obj:
                        q = obj[alt]
                        break
            elif isinstance(obj, str):
                q = obj

            if not isinstance(q, str) or not q.strip():
                i += 1
                continue

            items.append(
                {
                    "dataset_file": os.path.basename(p),
                    "index": i,
                    "question": q.strip(),
                    "raw": obj,
                }
            )
            i += 1
    return items


def open_outfile(path: str):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    return open(path, "a", encoding="utf-8")


def write_jsonl_line(fh, obj: Dict[str, Any]):
    fh.write(json.dumps(obj, ensure_ascii=False) + "\n")
    fh.flush()


# ---------------------------
# Provider test functions
# ---------------------------
async def test_grok_models(client, question: str):
    xai_key = os.getenv("XAI_API_KEY")
    if not xai_key or not GROK_MODELS:
        if not xai_key:
            print("❌ Skipping Grok models - XAI_API_KEY not set")
        return []

    print("\n🔍 Testing xAI Grok Models")
    print("=" * 40)
    results = []

    for model_id in GROK_MODELS:
        model_name = model_id.replace("-", " ").title()
        print(f"\n🤖 Testing {model_name} ({model_id})")
        try:
            config = LLMConfig(
                provider="grok",
                model=model_id,
                api_key=xai_key,
                temperature=0.7,
                max_tokens=10000,
            )
            start = time.time()
            messages = [Message(role="user", content=question)]
            response = await client.chat(messages=messages, config=config)
            dt = time.time() - start
            print(f"   ✅ Success! ({dt:.2f}s)")
            print(f"   📝 Response: {response.content[:100]}...")
            results.append({
                "provider": "grok",
                "model": model_id,
                "name": model_name,
                "success": True,
                "response_time": dt,
                "response": response.content,
            })
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            results.append({
                "provider": "grok",
                "model": model_id,
                "name": model_name,
                "success": False,
                "error": str(e),
            })
        await asyncio.sleep(1)

    return results


async def test_google_models(client, question: str):
    google_key = os.getenv("GOOGLE_API_KEY")
    if not google_key or not GOOGLE_MODELS:
        if not google_key:
            print("❌ Skipping Google models - GOOGLE_API_KEY not set")
        return []

    print("\n🔍 Testing Google (Gemini) Models")
    print("=" * 40)
    results = []

    use_vertex = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "true").lower() not in ("0", "false", "no")
    provider_specific = {
        "use_vertex_ai": use_vertex,
        "project": os.getenv("VERTEX_PROJECT"),
        "location": os.getenv("VERTEX_LOCATION", "us-central1"),
    }

    for model_id in GOOGLE_MODELS:
        model_name = model_id.replace("-", " ").title()
        print(f"\n🤖 Testing {model_name} ({model_id})")
        try:
            config = LLMConfig(
                provider="google",
                model=model_id,
                api_key=google_key,
                temperature=0.7,
                max_tokens=10000,
                provider_specific=provider_specific,
            )
            start = time.time()
            messages = [Message(role="user", content=question)]
            response = await client.chat(messages=messages, config=config)
            dt = time.time() - start
            print(f"   ✅ Success! ({dt:.2f}s)")
            print(f"   📝 Response: {response.content[:100]}...")
            results.append({
                "provider": "google",
                "model": model_id,
                "name": model_name,
                "success": True,
                "response_time": dt,
                "response": response.content,
            })
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            results.append({
                "provider": "google",
                "model": model_id,
                "name": model_name,
                "success": False,
                "error": str(e),
            })
        await asyncio.sleep(1)
    return results


async def test_openai_models(client, question: str):
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key or not OPENAI_MODELS:
        if not openai_key:
            print("❌ Skipping OpenAI models - OPENAI_API_KEY not set")
        return []

    print("\n🔍 Testing OpenAI Models")
    print("=" * 40)
    results = []

    for model_id in OPENAI_MODELS:
        model_name = model_id.replace("-", " ").title()
        print(f"\n🤖 Testing {model_name} ({model_id})")
        try:
            config = LLMConfig(
                provider="openai",
                model=model_id,
                api_key=openai_key,
                temperature=0.7,
                provider_specific={"max_completion_tokens": 5000},
            )
            start_time = time.time()
            messages = [Message(role="user", content=question)]
            response = await client.chat(messages=messages, config=config)
            end_time = time.time()
            response_time = end_time - start_time

            print(f"   ✅ Success! ({response_time:.2f}s)")
            print(f"   📝 Response: {response.content[:100]}...")

            results.append(
                {
                    "provider": "openai",
                    "model": model_id,
                    "name": model_name,
                    "success": True,
                    "response_time": response_time,
                    "response": response.content,
                }
            )
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            results.append(
                {
                    "provider": "openai",
                    "model": model_id,
                    "name": model_name,
                    "success": False,
                    "error": str(e),
                }
            )
        await asyncio.sleep(1)

    return results


async def test_claude_models(client, question: str):
    claude_key = os.getenv("CLAUDE_API_KEY")
    if not claude_key or not CLAUDE_MODELS:
        if not claude_key:
            print("❌ Skipping Claude models - CLAUDE_API_KEY not set")
        return []

    print("\n🔍 Testing Claude Models")
    print("=" * 40)
    results = []

    for model_id in CLAUDE_MODELS:
        model_name = model_id.replace("-", " ").title()
        print(f"\n🤖 Testing {model_name} ({model_id})")
        try:
            config = LLMConfig(
                provider="claude",
                model=model_id,
                api_key=claude_key,
                temperature=0.7,
                max_tokens=5000,
            )
            start_time = time.time()
            messages = [Message(role="user", content=question)]
            response = await client.chat(messages=messages, config=config)
            end_time = time.time()
            response_time = end_time - start_time

            print(f"   ✅ Success! ({response_time:.2f}s)")
            print(f"   📝 Response: {response.content[:100]}...")

            results.append(
                {
                    "provider": "claude",
                    "model": model_id,
                    "name": model_name,
                    "success": True,
                    "response_time": response_time,
                    "response": response.content,
                }
            )
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            results.append(
                {
                    "provider": "claude",
                    "model": model_id,
                    "name": model_name,
                    "success": False,
                    "error": str(e),
                }
            )
        await asyncio.sleep(1)

    return results


async def test_bedrock_models(client, question: str, region: str):
    aws_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_profile = os.getenv("AWS_PROFILE")
    if not (aws_key or aws_profile) or not BEDROCK_MODELS:
        if not (aws_key or aws_profile):
            print("❌ Skipping Bedrock models - AWS credentials not set")
        return []

    print(f"\n🔍 Testing AWS Bedrock Models (Region: {region})")
    print("=" * 50)
    results = []

    for model_id in BEDROCK_MODELS:
        model_name = (
            model_id.split(".")[-1].replace("-v1:0", "").replace("-v2:0", "").title()
        )
        print(f"\n🤖 Testing {model_name} ({model_id})")
        try:
            config = LLMConfig(
                provider="bedrock",
                model=model_id,
                temperature=0.7,
                max_tokens=5000,
                provider_specific={"region_name": region},
            )
            start_time = time.time()
            messages = [Message(role="user", content=question)]
            response = await client.chat(messages=messages, config=config)
            end_time = time.time()
            response_time = end_time - start_time

            print(f"   ✅ Success! ({response_time:.2f}s)")
            print(f"   📝 Response: {response.content[:100]}...")

            results.append(
                {
                    "provider": "bedrock",
                    "model": model_id,
                    "name": model_name,
                    "success": True,
                    "response_time": response_time,
                    "response": response.content,
                    "region": region,
                }
            )
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            results.append(
                {
                    "provider": "bedrock",
                    "model": model_id,
                    "name": model_name,
                    "success": False,
                    "error": str(e),
                    "region": region,
                }
            )
        await asyncio.sleep(1)

    return results


def print_summary(all_results: List[Dict[str, Any]]):
    if not all_results:
        print("\n❌ No results to summarize!")
        return

    successful = [r for r in all_results if r.get("success", False)]
    failed = [r for r in all_results if not r.get("success", False)]

    print(f"\n📊 SUMMARY")
    print("=" * 50)
    print(f"✅ Successful: {len(successful)}/{len(all_results)} models")
    print(f"❌ Failed: {len(failed)}/{len(all_results)} models")

    if successful:
        avg_time = sum(r["response_time"] for r in successful) / len(successful)
        fastest = min(successful, key=lambda x: x["response_time"])
        print(f"⏱️  Average response time: {avg_time:.2f}s")
        print(f"⚡ Fastest: {fastest['name']} ({fastest['response_time']:.2f}s)")

    by_provider = {}
    for result in successful:
        provider = result["provider"]
        by_provider[provider] = by_provider.get(provider, 0) + 1

    print(f"\n📈 Success by provider:")
    for provider, count in by_provider.items():
        total = len([r for r in all_results if r["provider"] == provider])
        print(f"   {provider.upper()}: {count}/{total}")

    if failed:
        print(f"\n❌ Failed models:")
        for result in failed:
            print(f"   • {result['name']}: {result.get("error", "Unknown error")}")


# ---------------------------
# Main
# ---------------------------
async def main():
    parser = argparse.ArgumentParser(
        description="Test multiple models with one question or a JSONL dataset"
    )
    parser.add_argument("--region", default=AWS_REGION, help="AWS region for Bedrock")
    parser.add_argument(
        "--question",
        default=TEST_QUESTION,
        help="Single question to ask all models (ignored if --dataset is provided)",
    )
    parser.add_argument(
        "--dataset",
        nargs="+",
        help="One or more JSONL files with questions/prompts",
    )
    parser.add_argument(
        "--field",
        default="question",
        help='JSON key that contains the prompt in each JSONL object (default: "question")',
    )
    parser.add_argument(
        "--out",
        default=f"outputs_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.jsonl",
        help="Output JSONL file to append results",
    )

    args = parser.parse_args()

    print("🚀 MULTI-MODEL TESTING")
    print("=" * 50)
    print(f"🌍 AWS Region: {args.region}")

    credentials = check_credentials()

    if args.dataset:
        dataset_items = load_questions_from_datasets(args.dataset, args.field)
        if not dataset_items:
            print("❌ No valid questions found in dataset(s). Exiting.")
            return
        print(f"🗂️  Loaded {len(dataset_items)} questions from {len(args.dataset)} dataset file(s).")
        questions_iterable = dataset_items
    else:
        questions_iterable = [
            {
                "dataset_file": None,
                "index": 0,
                "question": args.question,
                "raw": {"question": args.question},
            }
        ]
        print(f"📝 Single Question: {args.question}")

    client = MultiLLM()

    with open_outfile(args.out) as out_fh:
        print(f"💾 Writing results to: {args.out}")
        all_results_for_summary = []

        for item in questions_iterable:
            q_text = item["question"]
            print("\n" + "-" * 50)
            if item["dataset_file"] is not None:
                print(f"▶️  Running for dataset '{item['dataset_file']}' entry #{item['index']}: {q_text}")
            else:
                print(f"▶️  Running for single question: {q_text}")

            # --- OpenAI ---
            if credentials.get("openai"):
                openai_results = await test_openai_models(client, q_text)
                all_results_for_summary.extend(openai_results)
                for r in openai_results:
                    write_jsonl_line(
                        out_fh,
                        {
                            "timestamp_utc": datetime.utcnow().isoformat(),
                            "dataset_file": item["dataset_file"],
                            "dataset_index": item["index"],
                            "question": q_text,
                            "provider": r.get("provider"),
                            "model": r.get("model"),
                            "region": r.get("region"),
                            "success": r.get("success", False),
                            "response_time": r.get("response_time"),
                            "response": r.get("response"),
                            "error": r.get("error"),
                            "raw_item": item["raw"],
                        },
                    )

            # --- Claude ---
            if credentials.get("claude"):
                claude_results = await test_claude_models(client, q_text)
                all_results_for_summary.extend(claude_results)
                for r in claude_results:
                    write_jsonl_line(
                        out_fh,
                        {
                            "timestamp_utc": datetime.utcnow().isoformat(),
                            "dataset_file": item["dataset_file"],
                            "dataset_index": item["index"],
                            "question": q_text,
                            "provider": r.get("provider"),
                            "model": r.get("model"),
                            "region": r.get("region"),
                            "success": r.get("success", False),
                            "response_time": r.get("response_time"),
                            "response": r.get("response"),
                            "error": r.get("error"),
                            "raw_item": item["raw"],
                        },
                    )

            # --- Bedrock ---
            if credentials.get("bedrock"):
                bedrock_results = await test_bedrock_models(client, q_text, args.region)
                all_results_for_summary.extend(bedrock_results)
                for r in bedrock_results:
                    write_jsonl_line(
                        out_fh,
                        {
                            "timestamp_utc": datetime.utcnow().isoformat(),
                            "dataset_file": item["dataset_file"],
                            "dataset_index": item["index"],
                            "question": q_text,
                            "provider": r.get("provider"),
                            "model": r.get("model"),
                            "region": r.get("region"),
                            "success": r.get("success", False),
                            "response_time": r.get("response_time"),
                            "response": r.get("response"),
                            "error": r.get("error"),
                            "raw_item": item["raw"],
                        },
                    )

            # --- Google (Gemini) ---
            if credentials.get("google"):
                google_results = await test_google_models(client, q_text)
                all_results_for_summary.extend(google_results)
                for r in google_results:
                    write_jsonl_line(
                        out_fh,
                        {
                            "timestamp_utc": datetime.utcnow().isoformat(),
                            "dataset_file": item["dataset_file"],
                            "dataset_index": item["index"],
                            "question": q_text,
                            "provider": r.get("provider"),
                            "model": r.get("model"),
                            "region": r.get("region"),
                            "success": r.get("success", False),
                            "response_time": r.get("response_time"),
                            "response": r.get("response"),
                            "error": r.get("error"),
                            "raw_item": item["raw"],
                        },
                    )

            # --- Grok (xAI) ---
            if credentials.get("grok"):
                grok_results = await test_grok_models(client, q_text)
                all_results_for_summary.extend(grok_results)
                for r in grok_results:
                    write_jsonl_line(
                        out_fh,
                        {
                            "timestamp_utc": datetime.utcnow().isoformat(),
                            "dataset_file": item["dataset_file"],
                            "dataset_index": item["index"],
                            "question": q_text,
                            "provider": r.get("provider"),
                            "model": r.get("model"),
                            "region": r.get("region"),
                            "success": r.get("success", False),
                            "response_time": r.get("response_time"),
                            "response": r.get("response"),
                            "error": r.get("error"),
                            "raw_item": item["raw"],
                        },
                    )

        print_summary(all_results_for_summary)
        print(f"\n🎉 Completed! Total model calls: {len(all_results_for_summary)}")
        print(f"💾 Results appended to: {args.out}")


if __name__ == "__main__":
    asyncio.run(main())
