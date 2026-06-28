import json

from feature_engineering import calculate_final_score

DATA_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

results = []

print("Evaluating ranking model...\n")

with open(DATA_FILE, "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        score = calculate_final_score(candidate)

        results.append(
            (
                score,
                candidate["profile"].get("headline", ""),
                candidate["profile"].get("current_title", "")
            )
        )

results.sort(reverse=True)

top100 = results[:100]

titles = {}

for _, _, title in top100:

    title = title.strip()

    titles[title] = titles.get(title, 0) + 1

print("=" * 60)
print("TOP 100 TITLE DISTRIBUTION")
print("=" * 60)

for title, count in sorted(
        titles.items(),
        key=lambda x: x[1],
        reverse=True):

    print(f"{title:35} {count}")

print("\n")

ai_keywords = [
    "ai",
    "ml",
    "machine learning",
    "search",
    "recommendation",
    "retrieval",
    "nlp",
    "applied scientist",
    "data scientist",
]

matches = 0

for _, headline, title in top100:

    text = (headline + " " + title).lower()

    if any(k in text for k in ai_keywords):
        matches += 1

print("=" * 60)
print(f"AI-related candidates in Top100 : {matches}/100")
print("=" * 60)