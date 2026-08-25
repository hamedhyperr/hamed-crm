import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hamed Automation CRM", layout="wide")
st.title("Hamed Automation CRM - Industrial Marketing")

data = {
    "Lead ID": ["IND-001", "IND-002", "SHH-001", "SAF-001"],
    "Business Name": ["Tarashkari Pars", "Sanaye Choob Arya", "Pooshak Sarina", "Mekanik Part"],
    "Industry": ["Machinery", "Wood and Cabinet", "Textile", "Industrial Parts"],
    "City": ["Safadasht", "Safadasht", "Shahriar", "Shamsabad"],
    "Status": ["New", "Contacted", "New", "Deal Closed"],
    "Phone": ["09121111111", "09122222222", "09123333333", "09124444444"]
}
df = pd.DataFrame(data)

st.subheader("Active Leads Database")
st.dataframe(df, use_container_width=True)
