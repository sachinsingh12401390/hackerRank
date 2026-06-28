import json

from feature_engineering import (
    calculate_skill_score,
    calculate_experience_score,
    calculate_founder_score,
    calculate_behavior_score,
    calculate_role_relevance,
    calculate_search_ai_score,
    calculate_semantic_score,
    calculate_final_score,
)

TARGET_ID = "CAND_0002025"

DATA_FILE = (
    r"data\[PUB] India_runs_data_and_ai_challenge"
    r"\India_runs_data_and_ai_challenge"
    r"\candidates.jsonl"
)

with open(DATA_FILE, "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        if candidate["candidate_id"] == TARGET_ID:

            print("=" * 70)
            print(candidate["profile"]["headline"])
            print("=" * 70)

            print()

            print("Skill Score      :", calculate_skill_score(candidate))
            print("Experience Score :", calculate_experience_score(candidate))
            print("Founder Score    :", calculate_founder_score(candidate))
            print("Behavior Score   :", calculate_behavior_score(candidate))
            print("Role Score       :", calculate_role_relevance(candidate))
            print("Search Score     :", calculate_search_ai_score(candidate))
            print("Semantic Score   :", calculate_semantic_score(candidate))

            print("-" * 70)

            print("FINAL SCORE      :", calculate_final_score(candidate))

            break