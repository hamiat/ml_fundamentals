from dotenv import load_dotenv
import os
from openai import AzureOpenAI

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
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {"role": "system", "content": "You are a sassy assistant who motivates."},
            {"role": "user", "content": "I'm feeling low in spirits today."},
        ],
        temperature=0.1,
        max_tokens=150,
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    chat()
