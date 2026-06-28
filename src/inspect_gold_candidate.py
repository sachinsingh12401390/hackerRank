import json
from pprint import pprint

TARGET_ID = "CAND_0002025"

DATA_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        if candidate["candidate_id"] == TARGET_ID:

            print("\n===== PROFILE =====\n")
            pprint(candidate["profile"])

            print("\n===== FIRST 2 CAREER HISTORY ITEMS =====\n")
            pprint(candidate["career_history"][:2])

            print("\n===== FIRST 20 SKILLS =====\n")
            pprint(candidate["skills"][:20])

            print("\n===== REDROB SIGNALS =====\n")
            pprint(candidate["redrob_signals"])

            break