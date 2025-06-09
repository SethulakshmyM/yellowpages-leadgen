# app.py

import streamlit as st
import pandas as pd
from LeadGenTool import get_leads

st.set_page_config(page_title="Lead Generator", layout="centered")
st.title("🔍 YellowPages Lead Generator")

st.write("Quickly generate business leads by scraping YellowPages for a given service and location.")

with st.form("lead_form"):
    keyword = st.text_input("Enter a service keyword", placeholder="e.g., dentist, plumber, law firm")
    location = st.text_input("Enter a location", placeholder="e.g., New York, NY")
    pages = st.slider("Number of pages to scrape", 1, 5, 1)
    submitted = st.form_submit_button("Scrape Leads")

if submitted:
    if not keyword or not location:
        st.error("❗ Please fill in both keyword and location.")
    else:
        with st.spinner("🔄 Scraping..."):
            leads = get_leads(keyword, location, pages)

        if leads.empty:
            st.warning("⚠️ No leads found. Try different input or fewer pages.")
        else:
            st.success(f"✅ {len(leads)} leads found!")
            st.dataframe(leads)
            csv = leads.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name=f'leads_{keyword}_{location}.csv',
                mime='text/csv'
            )
