import streamlit as st
from groq import Groq

st.set_page_config(page_title="My ChatGPT", page_icon="🤖")
st.title("My AI Assistant 🤖")

# Apni Groq API Key yahan dalein
client = Groq(api_key="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")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_input := st.chat_input("Kuch bhi poochaen..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=st.session_state.messages,
            stream=True
        )
        
        for chunk in completion:
            if chunk.choices.delta.content:
                full_response += chunk.choices.delta.content
                response_placeholder.write(full_response)
                
        st.session_state.messages.append({"role": "assistant", "content": full_response})
