import streamlit as st
# Import Week 8 database connection
from app.data.db import connect_database
# Import Week 8 CRUD functions for each domain
from app.data.users import verify_user, get_user_role
from app.data.datasets import get_all_datasets
from app.data.tickets import get_all_tickets
import pandas as pd

st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg", caption = "streamlit logo", use_container_width= True)

df = pd.DataFrame(
    {
        'name': ["Stevan", "Olaf", "Djani"],
        'age': [19, 18, 19]

    }
)
st.dataframe(df)
st.title("Hello, Streamlit! 👋")
st.write("This is my very first Streamlit app. ")
st.header("Hello this is header 😊")
st.subheader("This is sub header")
st.write("aaaaaaaaa")
st.markdown("This is the markdown")
st.caption("TS the caption")
st.text("this is evil text")
st.text("This is continuation")

name = st.text_input("Enter name: ")
st.write(f"The username is {name}")
if st.button("submit"):
    if name:
        st.success(f"Hello, You")
    else:
        st.warning("Enter name")

age = st.number_input(
"Age", min_value=0,
 max_value=120, value=25
 )

st.write(age)
if age < 18:
    st.balloons()

# At the top of your Streamlit page (e.g., pages/1_Dashboard.py)

import streamlit as st


