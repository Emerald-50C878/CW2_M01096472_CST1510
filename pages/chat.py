import streamlit as st
from openai import OpenAI

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

inp = st.chat_input("You: ")

if inp:
    st.session_state.messages.append({"role": "user", "content": inp})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(inp)

def chat_interface():
    st.title("Chat with GPT-5.1")

    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if user_input:
            

            client = OpenAI(api_key="your-api-key-here")

            completion = client.chat.completions.create(
                model="gpt-5.1",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            response = completion.choices[0].message.content
            st.text_area("GPT-5.1:", value=response, height=200)
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})