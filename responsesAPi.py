import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import streamlit as st

load_dotenv()
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version="2025-03-01-preview",
)

def chat():
    st.title(":rainbow[Hami's Chat bot] \U0001F920")
    st.write("Let's have chat, fam!")

    user_input = st.text_input("Your message:")

    if "previous_response_id" not in st.session_state:
        st.session_state.previous_response_id = None

    tone = "You are an empathetic assistant. Respond warmly and encourage users gently."
    max_tokens = 300
    temp = 0.5

    if user_input:
        with st.spinner("Let me think..."):
            response = client.responses.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            instructions=tone,
            input= user_input,
            previous_response_id=st.session_state.previous_response_id,
            temperature=temp,
            max_output_tokens=max_tokens
            )
    
        st.markdown(f"Chat: {response.output_text}")

        st.session_state.previous_response_id = response.id

        if hasattr(response, "usage"):
            usage = response.usage
            st.markdown(f"**Tokens used: {usage.total_tokens}**")


if __name__ == "__main__":
    chat()