import os
os.environ["TAVILY_API_KEY"] = "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"
from fastapi import FastAPI
from research_agent import search_web
from answer_agent import generate_answer


app = FastAPI()

@app.get("/search")
def research(query: str):
    research_results = search_web(query)
    response = generate_answer(research_results)
    return {"answer": response}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
