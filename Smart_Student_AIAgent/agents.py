from dataclasses import dataclass
from typing import Callable, List, Any, Dict, Optional

# ---------- Decorator to mark a function as a tool ----------
def function_tool(func: Callable) -> Callable:
    """
    Marks a function as an agent tool.
    """
    setattr(func, "__is_tool__", True)
    setattr(func, "__tool_name__", func.__name__)
    setattr(func, "__tool_doc__", (func.__doc__ or "").strip())
    return func

# ---------- Agent definition ----------
@dataclass
class Agent:
    name: str
    instructions: str
    tools: List[Callable]

# ---------- Run result ----------
@dataclass
class RunResult:
    final_output: str
    tool_used: Optional[str] = None
    meta: Dict[str, Any] = None

# ---------- Runner class ----------
class Runner:
    @staticmethod
    def select_tool(agent: Agent, query: str) -> Callable:
        """
        Selects the best tool based on the query.
        """
        q = query.lower().strip()
        # heuristic matching
        if any(k in q for k in ["summarize", "summary", "tl;dr"]):
            for t in agent.tools:
                if t.__name__ == "summarize_text":
                    return t
        if any(k in q for k in ["tip", "study plan", "study tips", "how to study", "revision"]):
            for t in agent.tools:
                if t.__name__ == "study_tips":
                    return t
        # default to answer_question if available
        for t in agent.tools:
            if t.__name__ == "answer_question":
                return t
        # fallback → return first tool
        return agent.tools[0]

    @staticmethod
    def run_sync(agent: Agent, query: str) -> RunResult:
        """
        Runs the selected tool synchronously.
        """
        tool = Runner.select_tool(agent, query)
        try:
            output = tool(query)  # tool accepts the query
        except TypeError:
            # if tool does not accept args
            output = tool()
        return RunResult(
            final_output=output,
            tool_used=getattr(tool, "__tool_name__", tool.__name__),
            meta={}
        )
