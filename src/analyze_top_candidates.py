import json

from feature_engineering import calculate_final_score

DATA_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

results = []

with open(DATA_FILE, "r", encoding="utf-8") as f:

    for i, line in enumerate(f):

        candidate = json.loads(line)

        score = calculate_final_score(candidate)

        results.append(
            (
                score,
                candidate
            )
        )

        if i >= 999:
            break

results.sort(
    key=lambda x: x[0],
    reverse=True
)

for rank, (score, candidate) in enumerate(results[:10], start=1):

    profile = candidate["profile"]

    print("\n" + "=" * 80)

    print(f"RANK #{rank}")
    print(f"Score: {score}")

    print(
        f"Candidate ID: {candidate['candidate_id']}"
    )

    print(
        f"Headline: {profile.get('headline')}"
    )

    print(
        f"Current Title: {profile.get('current_title')}"
    )

    print(
        f"Company: {profile.get('current_company')}"
    )

    print(
        f"Experience: {profile.get('years_of_experience')}"
    )

    print("\nSUMMARY:")

    print(
        profile.get("summary", "")[:600]
    )