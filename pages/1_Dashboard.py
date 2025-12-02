import streamlit as st
import pandas as pd
from app.data.db import connect_database
from app.data.incidents import get_all_incidents
from app.data.datasets import get_all_datasets
from app.data.tickets import get_all_tickets
 
# Ensures only signed-in users can reach this page.
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be signed in to view this page.")
    if st.button("Return to Login"):
        st.switch_page("Home.py")
    st.stop()
 
st.title(" Dashboard")
st.success(f"Welcome, {st.session_state.username}!")
 
# Connect to the database so the tables can be loaded.
conn = connect_database()
 
# Display cyber incident records.
st.header("Cyber Incidents")
st.dataframe(get_all_incidents(conn), use_container_width=True)
 
# Display dataset information.
st.header("Datasets")
st.dataframe(get_all_datasets(conn), use_container_width=True)
 
# Display IT ticket information.
st.header("IT Tickets")
st.dataframe(get_all_tickets(conn), use_container_width=True)
 
st.divider()
 
# Allows the user to sign out.
if st.button("Log Out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("Home.py")
 
# Connect to database (Week 8 function)
conn = connect_database('DATA/intelligence_platform.db')
# Page title
st.title("Cyber Incidents Dashboard")

# READ: Display incidents in a beautiful table (Week 8 function + Streamlit UI)
incidents = get_all_incidents(conn) # ← Week 8 function handles SQL
st.dataframe(incidents, use_container_width=True) # ← Streamlit creates UI

# CREATE: Add new incident with a form
with st.form("new_incident"):
# Form inputs (Streamlit widgets)
 title = st.text_input("Incident Title")
 severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
 status = st.selectbox("Status", ["Open", "In Progress", "Resolved"])

# Form submit button
 submitted = st.form_submit_button("Add Incident")

# When form is submitted
if submitted and title:
    # Call Week 8 function to insert into database
    insert_incident(conn, title, severity, status) # ← Week 8 function!
    st.success("✓ Incident added successfully!")
    st.rerun() # Refresh the page to show new incident