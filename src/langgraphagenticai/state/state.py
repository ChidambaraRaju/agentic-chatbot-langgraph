from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    Represents the state of the agent.
    """
    messages: Annotated[List[str], add_messages]
    