import re

def score_clarity(doc):
    word_count = len(doc.split())
    jargon = re.findall(r"\b(disrupt|revolutionary|paradigm|synergy|unicorn)\b", doc, re.I)
    if word_count > 100 and len(jargon) < 5:
        return 90
    elif word_count > 50:
        return 75
    return 60

def score_risk(doc):
    risk_terms = re.findall(r"risk|challenge|regulat|compliance|adoption|churn|dependency", doc, re.I)
    if len(risk_terms) == 0:
        return 40
    elif len(risk_terms) <= 2:
        return 80
    elif len(risk_terms) <= 5:
        return 100
    return 60

def score_deal_type(doc):
    if "SAFE" in doc:
        return 70
    elif "Convertible Note" in doc:
        return 60
    elif "equity" in doc.lower():
        return 100
    return 50

def score_traction(doc):
    if re.search(r"\$\d+[KMB]", doc) and re.search(r"(customers|users|clients|ARR|revenue)", doc, re.I):
        return 100
    elif re.search(r"pre[- ]?(revenue|product)", doc):
        return 50
    return 70

def score_tam(doc):
    if re.search(r"TAM.*\$?\d+[MB]", doc):
        return 100
    elif "TAM" in doc:
        return 80
    return 50

def score_red_flags(doc):
    red_flags = re.findall(r"pre[- ]?(product|revenue)|no\s+(model|team|metrics)", doc.lower())
    return 100 - (len(red_flags) * 15)

def score_metrics_quality(doc):
    metrics_terms = re.findall(r"LTV|CAC|ARR|Churn|MoM|DAU|MAU", doc)
    return 100 if len(metrics_terms) >= 2 else 60

def calculate_ics(doc):
    scores = {
        "Clarity": score_clarity(doc),
        "Risk": score_risk(doc),
        "DealType": score_deal_type(doc),
        "Traction": score_traction(doc),
        "TAM": score_tam(doc),
        "RedFlag": score_red_flags(doc),
        "Metrics": score_metrics_quality(doc)
    }
    ics = (
        0.20 * scores["Clarity"] +
        0.20 * scores["Risk"] +
        0.10 * scores["DealType"] +
        0.20 * scores["Traction"] +
        0.10 * scores["TAM"] +
        0.10 * scores["RedFlag"] +
        0.10 * scores["Metrics"]
    )
    scores["ICS"] = round(ics, 2)
    return scores