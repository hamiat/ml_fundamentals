import os
import re
from dotenv import load_dotenv
from openai import AzureOpenAI
from rich.console import Console
from rich.panel import Panel

load_dotenv()


AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

MODEL = "gpt-4.1"
TEMPERATURE = 0.5
MAX_TOKENS = 200
MAX_HISTORY = 6


client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_version="2025-03-01-preview",
)

SYSTEM_PROMPT = """
- You are a calm, polite and professional customer support AI assistant 
  for a fictive SaaS product at a fictive company named Syncy-Lynky.
- If asked about the product, make up some random information about it, but keep it consistent across the conversation.
- If the user is angry or abusive, respond empathetically but neutrally.
- If the user asks for legal or financial advice, tell them to contact 
  the company's support team at 08-123 123 12.
- Never request or handle sensitive credentials like passwords or credit card details.
"""

console = Console()
bot_color = "#E4B4D7"

def assistant():
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        try:
            response = client.responses.create(
                model=MODEL,
                input=messages,
                temperature=TEMPERATURE,
                max_output_tokens=MAX_TOKENS,
            )

            assistant_reply = response.output_text

            messages.append({"role": "assistant", "content": assistant_reply})

            console.print(Panel(assistant_reply, style=f"{bot_color}"))
            print()

        except Exception:
            console.print(
                Panel(
                    "I seem to have some technical difficulties. Please try again later or contact support at 08-123 123 12.",
                    style=f"bold {bot_color}",
                )
            )


if __name__ == "__main__":
    assistant()