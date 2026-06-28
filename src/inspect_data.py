import json
from pprint import pprint

DATA_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    first_candidate = json.loads(next(f))

print("\n===== PROFILE =====\n")
pprint(first_candidate["profile"])

print("\n===== CAREER HISTORY SAMPLE =====\n")
pprint(first_candidate["career_history"][:1])

print("\n===== SKILLS =====\n")
pprint(first_candidate["skills"][:10])

print("\n===== REDROB SIGNALS =====\n")
pprint(first_candidate["redrob_signals"])