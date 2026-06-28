import json

from explainer import explain_candidate

with open(r"data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl", "r", encoding="utf-8") as f:

    candidate = json.loads(next(f))

print(explain_candidate(candidate))