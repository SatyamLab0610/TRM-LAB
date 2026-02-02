def classify_site(page_text, addresses):
    keywords = [
        "deposit","withdraw","investment","profit",
        "guaranteed","wallet","crypto","usdt","trading"
    ]

    score = sum(1 for k in keywords if k in page_text.lower())
    if addresses:
        score += 3

    if score >= 4:
        return "SCAM", min(score / 8, 1.0)

    return "NOT_SCAM", score / 8
