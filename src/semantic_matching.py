from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from job_description import JOB_DESCRIPTION

model = SentenceTransformer("all-MiniLM-L6-v2")

JOB_EMBEDDING = model.encode(
    JOB_DESCRIPTION,
    convert_to_numpy=True,
    normalize_embeddings=True
)


def build_candidate_text(candidate):

    profile = candidate.get("profile", {})

    parts = []

    parts.append(profile.get("headline", ""))
    parts.append(profile.get("current_title", ""))
    parts.append(profile.get("summary", ""))

    for skill in candidate.get("skills", []):
        parts.append(skill.get("name", ""))

    for job in candidate.get("career_history", []):
        parts.append(job.get("title", ""))
        parts.append(job.get("description", ""))

    return " ".join(parts)


def semantic_similarity(candidate):

    candidate_text = build_candidate_text(candidate)

    candidate_embedding = model.encode(
        candidate_text,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    similarity = cosine_similarity(
        candidate_embedding.reshape(1, -1),
        JOB_EMBEDDING.reshape(1, -1)
    )[0][0]

    return round(similarity * 100, 2)