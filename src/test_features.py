import json

from feature_engineering import (
    calculate_skill_score,
    calculate_experience_score,
    calculate_founder_score,
    calculate_behavior_score,
    calculate_final_score
)

DATA_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    candidate = json.loads(next(f))

print("Skill Score:", calculate_skill_score(candidate))
print("Experience Score:", calculate_experience_score(candidate))
print("Founder Score:", calculate_founder_score(candidate))
print("Behavior Score:", calculate_behavior_score(candidate))
role_score = calculate_role_relevance(candidate)

final_score = (
    0.25 * skill_score
    + 0.20 * experience_score
    + 0.15 * founder_score
    + 0.20 * behavior_score
    + 0.20 * role_score
)
