from candidate_analyzer import (
    company_type,
    has_search_experience,
)


def explain_candidate(candidate):

    reasons = []

    profile = candidate.get("profile", {})
    signals = candidate.get("redrob_signals", {})

    ####################################
    # Search / Retrieval
    ####################################

    search_hits = has_search_experience(candidate)

    if len(search_hits) >= 3:
        reasons.append(
            "Strong Search / Retrieval experience"
        )
    elif len(search_hits) > 0:
        reasons.append(
            "Some Search / Retrieval experience"
        )

    ####################################
    # Company
    ####################################

    company = company_type(candidate)

    if company == "product":
        reasons.append(
            "Product company experience"
        )

    elif company == "service":
        reasons.append(
            "IT services background"
        )

    ####################################
    # Experience
    ####################################

    years = profile.get(
        "years_of_experience",
        0
    )

    if years >= 5:
        reasons.append(
            f"{years:.1f}+ years experience"
        )

    ####################################
    # Open to work
    ####################################

    if signals.get(
        "open_to_work_flag",
        False
    ):
        reasons.append(
            "Open to work"
        )

    ####################################
    # Recruiter response
    ####################################

    if signals.get(
        "recruiter_response_rate",
        0
    ) >= 0.60:

        reasons.append(
            "High recruiter response rate"
        )

    ####################################
    # GitHub
    ####################################

    if signals.get(
        "github_activity_score",
        0
    ) >= 70:

        reasons.append(
            "Strong GitHub activity"
        )

    ####################################
    # Notice Period
    ####################################

    notice = signals.get(
        "notice_period_days",
        999
    )

    if notice <= 30:
        reasons.append(
            "Short notice period"
        )

    ####################################
    # Relocation
    ####################################

    if signals.get(
        "willing_to_relocate",
        False
    ):

        reasons.append(
            "Willing to relocate"
        )

    return reasons