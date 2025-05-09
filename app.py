import os
import fitz
import streamlit as st
import requests
from bs4 import BeautifulSoup
from engine.ics_engine import calculate_ics
from supabase import create_client, Client
import json

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY", "")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="dude dq | due diligence ai", layout="centered")
st.markdown("<style>body { font-family: Arial, sans-serif; }</style>", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <div style='width: 50px; height: 50px; background: black; margin: auto;'></div>
        <h1 style='font-size: 2.4rem; margin: 0.5rem 0;'>dude dq</h1>
        <p style='font-size: 1rem; color: #444;'>startup due diligence analysis, powered by ai. open source. always simple.</p>
    </div>
""", unsafe_allow_html=True)

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    texts = soup.find_all(['p', 'h1', 'h2', 'li', 'span'])
    return "\n".join([t.get_text(strip=True) for t in texts])

st.subheader("Analyze a startup document")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
url = st.text_input("Or paste a public startup campaign page URL")
consent = st.checkbox("I agree to the Terms and Privacy Policy. I understand my uploaded content may be stored anonymously and used to generate aggregated insights.")

if consent:
    text_data = None
    if uploaded_file:
        text_data = extract_text_from_pdf(uploaded_file)
    elif url:
        try:
            text_data = extract_text_from_url(url)
        except:
            st.error("Could not fetch the URL.")

    if text_data:
        with st.spinner("Scoring startup..."):
            scores = calculate_ics(text_data)
            supabase.table("uploads").insert({
                "source_type": "upload" if uploaded_file else "url",
                "text_data": text_data[:5000],
                "ics_score": scores["ICS"],
                "score_json": json.dumps(scores)
            }).execute()
            st.success("Investor Confidence Score (ICS):")
            st.json(scores)
else:
    st.info("Please agree to the Terms before proceeding.")

st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 0.8rem; color: #777;'>
        © 2025 dude dq · open source under MIT license · this site collects anonymized startup document data for research and benchmarking purposes only.
    </p>
""", unsafe_allow_html=True)