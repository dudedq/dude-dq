# dude dq

**dude dq** is an open-source, AI-powered due diligence assistant for evaluating startup investment materials. It analyzes pitch decks, investment memos, or campaign links and generates an Investor Confidence Score (ICS) — all in one streamlined, privacy-respecting experience.

## 🔍 Features
- Single-page Streamlit app with upload + output
- Uses `supabase` for secure, consent-based data capture
- NLP-based scoring engine (ICS) + OpenAI GPT-ready
- Clean design: Arial font, black & white, minimal
- Built-in real startup-style test data (no fake fluff)
- Legal + compliant (user consent checkbox, no PII stored)
- MIT licensed (open-source and customizable)

## 📂 Uploads Table Schema (Supabase)

| Column        | Type     | Description                    |
|---------------|----------|--------------------------------|
| id            | UUID     | Primary key                    |
| inserted_at   | Timestamp| Auto timestamp                 |
| source_type   | Text     | 'upload' or 'url'              |
| text_data     | Text     | Truncated (first 5000 chars)   |
| ics_score     | Float    | Composite 0–100 score          |
| score_json    | JSON     | Full detail of component scores|

## 🚀 Tech Stack
- **Frontend**: Streamlit (unified landing + scoring)
- **Backend**: Supabase (persistent logging)
- **Scoring**: NLP + heuristics (ICS engine)
- **AI-Ready**: Optional OpenAI GPT-4 integration
- **Deployment**: GitHub + Streamlit Cloud + GoDaddy domain

## 🛠️ Setup Instructions

### 1. Requirements
- Python 3.8+
- A Supabase project (free)
- Streamlit Cloud account
- Optional: OpenAI key

### 2. Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

### 3. Set Streamlit Secrets (Cloud)
```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-supabase-anon-key"
OPENAI_API_KEY = "your-optional-openai-key"
```

## 🔐 Privacy + Compliance
- User must check a consent box before submitting
- All data is anonymized and limited to 5000 characters
- No user info, no founder PII, no private equity advice
- Aggregated insights only — safe for research and benchmarking

## 🧪 Real Test Cases Included
Built-in sample data simulates:
- B2B Fintech w/ traction
- Pre-product AI infra
- AgTech pilot w/ SAFE round

## 👨‍⚖️ License
MIT — free to use, build on, or commercialize with attribution

---

### ✍️ Author
Built with precision by a founder operating at M7-CTO standards, democratizing early-stage investing through open AI.