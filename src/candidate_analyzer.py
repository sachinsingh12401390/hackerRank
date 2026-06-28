PRODUCT_COMPANIES = [
    "Google",
    "Apple",
    "Amazon",
    "Microsoft",
    "Meta",
    "Netflix",
    "Uber",
    "Dream11",
    "PhonePe",
    "Flipkart",
    "Swiggy",
    "Meesho",
    "Zomato",
    "Paytm",
    "Razorpay",
    "CRED",
    "Myntra",
]

SERVICE_COMPANIES = [
    "TCS",
    "Infosys",
    "Wipro",
    "Cognizant",
    "Capgemini",
    "Accenture",
    "HCL",
    "Tech Mahindra",
    "LTIMindtree",
    "Mindtree",
]


def get_candidate_summary(candidate):

    profile = candidate.get("profile", {})

    return {
        "title": profile.get("current_title", ""),
        "headline": profile.get("headline", ""),
        "company": profile.get("current_company", ""),
        "experience": profile.get(
            "years_of_experience",
            0
        ),
        "industry": profile.get(
            "current_industry",
            ""
        )
    }


def company_type(candidate):

    company = candidate.get(
        "profile",
        {}
    ).get(
        "current_company",
        ""
    )

    if company in PRODUCT_COMPANIES:
        return "product"

    if company in SERVICE_COMPANIES:
        return "service"

    return "unknown"


def has_search_experience(candidate):

    text = ""

    profile = candidate.get("profile", {})

    text += profile.get("headline", "") + " "
    text += profile.get("summary", "") + " "

    for job in candidate.get(
        "career_history",
        []
    ):

        text += job.get("title", "") + " "
        text += job.get("description", "") + " "

    text = text.lower()

    keywords = [

        "retrieval",
        "ranking",
        "recommendation",
        "recommendation system",
        "recommendation systems",
        "search",
        "bm25",
        "embedding",
        "embeddings",
        "vector",
        "vector search",
        "hybrid retrieval",
        "dense retrieval",
        "learning-to-rank",
        "reranking",
        "re-ranking",
        "pinecone",
        "weaviate",
        "faiss",
        "qdrant",
        "milvus",
        "elasticsearch",
        "opensearch",
        "sentence transformer",
        "candidate-jd",
        "matching",
    ]

    hits = []

    for keyword in keywords:

        if keyword in text:
            hits.append(keyword)

    return list(set(hits))