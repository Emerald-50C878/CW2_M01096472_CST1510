import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cyber Incidents", page_icon="🛡️", layout="wide")

# --- Authorisation check ---
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("Please log in first.")
    st.switch_page("Home.py")

st.title("🛡️ Cyber Incidents Dashboard")
st.subheader("Overview of recent cyber security incidents 🚨")

@st.cache_data
def load_data():
    return pd.read_csv("DATA/cyber_incidents.csv")

df = load_data()

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    cols = df.columns.tolist()
    group_col = st.selectbox("Group by column", cols)

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Incidents by category")
    counts = df[group_col].value_counts()
    st.bar_chart(counts)

with col2:
    st.subheader("📊 Raw Data")
    st.dataframe(df)

