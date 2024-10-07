import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # Adds higher directory to python modules path.
from models.openai import Generator
import streamlit as st

def test():
    state = st.session_state
    # col1, col2 = st.columns([1, 1])
    with st.sidebar:
        st.subheader("LangGPT Structured Prompt")
        prompt = st.text_area("langgpt_prompt", state.prompt, height=500, label_visibility="collapsed")
        if st.button("Save Prompt"):
            if "test_messages" not in state:
                state.test_messages = []
            # state.test_messages = [{"role": "system", "content": prompt}]
            state.prompt = prompt
            st.rerun()

    ## A Chatbot to display the messages
    if "test_messages" not in state:
        state.test_messages = [{"role": "system", "content": state.prompt}]
        response = state.generator.generate_response(state.test_messages)
        state.test_messages.append({"role": "assistant", "content": response})
        st.rerun()

    # st.subheader("LangGPT Dialogue")
    for message in state.test_messages:
        if message["role"] == "system":
            continue
        st.chat_message(message["role"]).write(message["content"])
    
    if prompt := st.chat_input("Enter dialogue"):
        state.test_messages.append({"role": "user", "content": prompt})
        response = state.generator.generate_response(state.test_messages)
        state.test_messages.append({"role": "assistant", "content": response})
        st.rerun()