from semantic_matching import semantic_similarity
from jd_config import (
    TARGET_SKILLS,
    RELEVANT_TITLES,
    BAD_TITLES,
)


# ---------------------------------------------------
# Skill Score
# ---------------------------------------------------
def calculate_skill_score(candidate):

    score = 0

    for skill in candidate.get("skills", []):

        skill_name = skill.get("name", "").lower()

        for target_skill, weight in TARGET_SKILLS.items():

            if target_skill in skill_name:
                score += weight

    return min(score, 100)


# ---------------------------------------------------
# Experience Score
# ---------------------------------------------------
def calculate_experience_score(candidate):

    profile = candidate.get("profile", {})

    years = profile.get("years_of_experience")

    if years is None:

        total_months = sum(
            job.get("duration_months", 0)
            for job in candidate.get("career_history", [])
        )

        years = total_months / 12

    return min(years * 10, 100)


# ---------------------------------------------------
# Founder / Ownership Score
# ---------------------------------------------------
def calculate_founder_score(candidate):

    text = ""

    for job in candidate.get("career_history", []):
        text += job.get("description", "") + " "

    text = text.lower()

    keyword_weights = {
        "built": 15,
        "launched": 15,
        "owned": 12,
        "shipped": 12,
        "designed": 12,
        "architected": 15,
        "created": 10,
        "deployed": 12,
        "production": 10,
        "scaled": 15,
        "scaling": 15,
    }

    score = 0

    for keyword, weight in keyword_weights.items():

        if keyword in text:
            score += weight

    return min(score, 100)


# ---------------------------------------------------
# Behavior Score
# ---------------------------------------------------
def calculate_behavior_score(candidate):

    signals = candidate.get("redrob_signals", {})

    score = 0

    if signals.get("open_to_work_flag"):
        score += 20

    score += signals.get(
        "recruiter_response_rate",
        0
    ) * 20

    score += signals.get(
        "interview_completion_rate",
        0
    ) * 20

    score += min(
        signals.get("github_activity_score", 0),
        100
    ) * 0.10

    score += min(
        signals.get("saved_by_recruiters_30d", 20),
        20
    )

    score += min(
        signals.get("profile_completeness_score", 100),
        100
    ) * 0.10

    notice = signals.get(
        "notice_period_days",
        90
    )

    if notice <= 30:
        score += 10

    return round(min(score, 100), 2)


# ---------------------------------------------------
# Role Relevance
# ---------------------------------------------------
def calculate_role_relevance(candidate):

    profile = candidate.get("profile", {})

    text = (
        profile.get("headline", "") +
        " " +
        profile.get("current_title", "")
    ).lower()

    score = 0

    for title in RELEVANT_TITLES:

        if title in text:
            score += 20

    return min(score, 100)


# ---------------------------------------------------
# Bad Title Penalty
# ---------------------------------------------------
def calculate_penalty_score(candidate):

    title = (
        candidate
        .get("profile", {})
        .get("current_title", "")
        .lower()
    )

    for bad_title in BAD_TITLES:

        if bad_title in title:
            return 40

    return 0


# ---------------------------------------------------
# Search / Retrieval / RAG Score
# ---------------------------------------------------
def calculate_search_ai_score(candidate):

    profile = candidate.get("profile", {})

    text = (
        profile.get("headline", "") + " " +
        profile.get("summary", "") + " "
    )

    for job in candidate.get("career_history", []):

        text += job.get("title", "") + " "
        text += job.get("description", "") + " "

    text = text.lower()

    keywords = [
        "retrieval",
        "ranking",
        "recommendation",
        "recommendation systems",
        "search",
        "relevance",
        "matching",
        "embeddings",
        "embedding",
        "vector",
        "vector database",
        "rag",
        "llm",
        "learning-to-rank",
        "dense retrieval",
        "hybrid retrieval",
        "reranking",
        "re-ranking",
        "bm25",
        "faiss",
        "pinecone",
        "weaviate",
        "qdrant",
        "milvus",
        "opensearch",
        "elasticsearch",
        "sentence transformer",
    ]

    score = 0

    for keyword in keywords:

        if keyword in text:
            score += 8

    return min(score, 100)


# ---------------------------------------------------
# Semantic Score
# ---------------------------------------------------
def calculate_semantic_score(candidate):

    return semantic_similarity(candidate)


# ---------------------------------------------------
# Final Score
# ---------------------------------------------------
def calculate_final_score(candidate):

    skill = calculate_skill_score(candidate)
    experience = calculate_experience_score(candidate)
    founder = calculate_founder_score(candidate)
    behavior = calculate_behavior_score(candidate)
    role = calculate_role_relevance(candidate)
    search = calculate_search_ai_score(candidate)
    semantic = calculate_semantic_score(candidate)

    penalty = calculate_penalty_score(candidate)

    final = (
        skill * 0.15 +
        experience * 0.10 +
        founder * 0.10 +
        behavior * 0.10 +
        role * 0.10 +
        search * 0.20 +
        semantic * 0.25
    )

    final -= penalty

    return round(max(final, 0), 2)