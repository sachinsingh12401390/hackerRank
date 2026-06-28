import json
from pprint import pprint

TARGET_ID = "CAND_0000878"

DATA_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        if candidate["candidate_id"] == TARGET_ID:

            pprint(candidate["profile"])

            print("\nCAREER HISTORY\n")

            pprint(candidate["career_history"])

            break