from langchain_openai import ChatOpenAI
import os

# ✅ Ensure API Key is loaded correctly
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")

llm = ChatOpenAI(model_name="gpt-4", openai_api_key=OPENAI_API_KEY)

def generate_answer(data):
    response = llm.predict(f"Summarize the following information:\n\n{data}")
    return response

