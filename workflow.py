from langgraph.graph import StateGraph
from typing import TypedDict

# ✅ Define a state schema for data flow
class ResearchState(TypedDict):
    research_results: str  # Store research data
    final_answer: str  # Store processed answer

# ✅ Initialize StateGraph with state schema
workflow = StateGraph(ResearchState)

# ✅ Define processing function
def process_data(state: ResearchState):
    collected_data = state["research_results"]
    structured_response = f"Summarized Findings:\n\n{collected_data}"
    return {"final_answer": structured_response}

# ✅ Add nodes and edges
workflow.add_node("answer_agent", process_data)
workflow.add_edge("research_agent", "answer_agent")

