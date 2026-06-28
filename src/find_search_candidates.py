import json

KEYWORDS = [
    "retrieval",
    "ranking",
    "recommendation",
    "search",
    "embeddings",
    "vector",
    "relevance",
]

DATA_FILE = r"C:\Users\Sachin\Desktop\RecruitAI\data\[PUB] India_runs_data_and_ai_challenge\India_runs_data_and_ai_challenge\candidates.jsonl"

matches = []

with open(DATA_FILE, "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        text = ""

        text += candidate["profile"].get(
            "summary",
            ""
        )

        for job in candidate.get(
            "career_history",
            []
        ):
            text += " " + job.get(
                "description",
                ""
            )

        text = text.lower()

        hits = 0

        for keyword in KEYWORDS:
            if keyword in text:
                hits += 1

        if hits >= 3:

            matches.append(
                (
                    hits,
                    candidate
                )
            )

matches.sort(
    key=lambda x: x[0],
    reverse=True
)

for hits, candidate in matches[:20]:

    print("\n" + "=" * 80)

    print("Hits:", hits)

    print(
        candidate["candidate_id"]
    )

    print(
        candidate["profile"].get(
            "headline"
        )
    )