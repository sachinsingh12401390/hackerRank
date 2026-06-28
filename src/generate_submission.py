import json
import csv

from feature_engineering import calculate_final_score

DATA_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

OUTPUT_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\outputs\submission.csv"

results = []

print("Scoring candidates...")

with open(DATA_FILE, "r", encoding="utf-8") as f:
    for line in f:

        candidate = json.loads(line)

        score = calculate_final_score(candidate)

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": round(score, 2)
        })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "candidate_id",
        "score"
    ])

    for row in results:
        writer.writerow([
            row["candidate_id"],
            row["score"]
        ])

print("\nSubmission file saved successfully!")
print(OUTPUT_FILE)
print(f"\nTotal candidates: {len(results)}")