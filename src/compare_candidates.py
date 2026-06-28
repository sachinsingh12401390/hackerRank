import json

from feature_engineering import *

IDS = [
    "CAND_0000739",
    "CAND_0000031"
]

DATA_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

with open(DATA_FILE, "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] in IDS:

            print("\n" + "="*80)

            print(candidate["candidate_id"])

            print(candidate["profile"]["headline"])

            print()

            print("Skill:",
                  calculate_skill_score(candidate))

            print("Experience:",
                  calculate_experience_score(candidate))

            print("Founder:",
                  calculate_founder_score(candidate))

            print("Behavior:",
                  calculate_behavior_score(candidate))

            print("Role:",
                  calculate_role_relevance(candidate))

            print("Search AI:",
                  calculate_search_ai_score(candidate))

            print()

            print("FINAL:",
                  calculate_final_score(candidate))