# RecruitAI – Hybrid AI Candidate Ranking System

## Overview

RecruitAI is an intelligent candidate ranking system developed for the Data & AI Challenge.

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, which often misses highly qualified candidates whose experience is described differently.

RecruitAI combines semantic understanding with recruiter-inspired feature engineering to rank candidates based on their true suitability for a role rather than simple keyword overlap.

---

## Problem Statement

Recruiters must review thousands of resumes while trying to identify candidates who best fit a job description.

Keyword-based systems have several limitations:

* Miss candidates using different terminology
* Ignore behavioral hiring signals
* Ignore recruiter engagement signals
* Cannot understand semantic similarity
* Produce poor ranking quality

RecruitAI addresses these issues through a hybrid ranking architecture.

---

## Solution Architecture

The system combines two complementary approaches:

### 1. Feature Engineering

Domain-specific features are extracted from every candidate profile, including:

* Technical skills
* Years of experience
* Career history
* Founder / ownership signals
* Search & Retrieval expertise
* Recruiter behavioral signals
* Role relevance

### 2. Semantic Matching

Instead of relying only on keywords, RecruitAI converts both:

* Job Description
* Candidate Profile

into dense vector embeddings using the Sentence Transformer model:

```
all-MiniLM-L6-v2
```

Cosine similarity is then used to measure true semantic relevance.

---

## Hybrid Ranking Pipeline

```
Job Description
        │
        ▼
Sentence Transformer
        │
        ▼
Semantic Similarity
        │
        ▼
Feature Engineering
        │
        ▼
Hybrid Weighted Score
        │
        ▼
Ranked Candidates
```

---

## Features Used

### Candidate Skills

Weighted matching against required AI, Search and Retrieval technologies.

Examples:

* Python
* RAG
* LLM
* Retrieval
* Ranking
* Embeddings
* FAISS
* Pinecone
* Weaviate
* Elasticsearch

---

### Experience

Experience is estimated using:

* years_of_experience

or

* duration_months from career history

---

### Founder Mindset

Leadership and ownership keywords:

* Built
* Architected
* Designed
* Deployed
* Production
* Scaling
* Shipped

---

### Behavioral Signals

The model incorporates recruiter-focused signals:

* Open to Work
* Recruiter Response Rate
* Interview Completion Rate
* GitHub Activity
* Saved by Recruiters
* Profile Completeness
* Notice Period

---

### Role Relevance

Rewards candidates whose current role closely matches the target position.

Examples:

* AI Engineer
* ML Engineer
* Search Engineer
* Recommendation Systems Engineer
* NLP Engineer
* Applied Scientist

---

### Search / Retrieval Expertise

Special weighting for candidates with production search experience.

Examples:

* Retrieval
* Ranking
* Recommendation Systems
* Vector Search
* RAG
* FAISS
* Pinecone
* Qdrant
* BM25
* Learning-to-Rank

---

### Semantic Similarity

Dense embeddings generated using:

```
Sentence Transformers
```

Similarity metric:

```
Cosine Similarity
```

---

## Final Ranking Formula

```
15% Skill Score

10% Experience

10% Founder Signals

10% Behavioral Signals

10% Role Relevance

20% Search / Retrieval Expertise

25% Semantic Similarity

− Penalty for Irrelevant Roles
```

---

## Explainable AI

Each ranked candidate can be fully explained.

Example:

```
Skill Score       : 87

Experience Score : 78

Behavior Score   : 91

Semantic Score   : 82

Search Score     : 100

Final Score      : 70.28
```

---

## Evaluation

The model successfully prioritizes:

* Search Engineers
* Recommendation Engineers
* AI Engineers
* Applied Scientists
* NLP Engineers
* ML Engineers

while filtering unrelated professions.

---

## Tech Stack

* Python
* Sentence Transformers
* Scikit-Learn
* NumPy
* JSON
* CSV

---

## Repository Structure

```
src/
    feature_engineering.py
    semantic_matching.py
    rank_candidates.py
    generate_submission.py
    explain_candidate.py
    evaluate_model.py
    job_description.py
    jd_config.py

outputs/
    submission.csv
```

---

## Future Improvements

* Cross Encoder reranking
* LLM-based reasoning
* Vector Database
* Production REST API
* Learning-to-Rank models

---

## Author

Sachin

Built for the Data & AI Challenge 2026.
