import streamlit as st
import pandas as pd

st.set_page_config(page_title="IT Tickets", page_icon="🧩", layout="wide")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("Please log in first.")
    st.switch_page("Home.py")

st.title("🧩 IT Tickets Dashboard")
st.subheader("Overview of IT support tickets ⚙️")

@st.cache_data
def load_data():
    return pd.read_csv("DATA/it_tickets.csv")

df = load_data()

with st.sidebar:
    st.header("Filters")
    cols = df.columns.tolist()
    metric = st.selectbox("Select column to chart", cols)

st.line_chart(df[metric].value_counts())
st.dataframe(df)
