import json
from feature_engineering import calculate_final_score

# Dataset Path
DATA_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

results = []

print("Loading candidates and calculating scores...\n")

# Read every candidate in the dataset
with open(DATA_FILE, "r", encoding="utf-8") as f:
    for line in f:
        candidate = json.loads(line)

        score = calculate_final_score(candidate)

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": score,
            "headline": candidate["profile"].get("headline", "")
        })

# Sort by highest score
results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("=" * 80)
print("TOP 20 CANDIDATES")
print("=" * 80)

for i, candidate in enumerate(results[:20], start=1):
    print(
        f"{i:2}. "
        f"{candidate['candidate_id']} | "
        f"Score: {candidate['score']:.2f} | "
        f"{candidate['headline']}"
    )