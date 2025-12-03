import streamlit as st
# Import Week 8 database connection
from app.data.db import connect_database
# Import Week 8 CRUD functions for each domain
import pandas as pd
from app.data.cyber_incidents import get_all_cyber_incidents

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

data = get_all_cyber_incidents(conn)
st.title("Welcome to the home page")

print(data['severity'].unique())
'''
Index(['index', incident_id', 'timestamp', 'severity', 'category', status', 'description'],
    dtype= 'object')'''

st.write(data)
with st.sidebar:
    st.header("Navigation")
    st.selectbox('')
    severity_ = st.selectbox('severity', data['severity'].unique())

filtered_data = data[data['severity'] == severity_]

st.write(filtered_data)
# At the top of your Streamlit page (e.g., pages/1_Dashboard.py)



