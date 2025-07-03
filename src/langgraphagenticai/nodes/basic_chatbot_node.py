from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    A basic chatbot node that can be used in a LangGraph workflow.
    This node can be used to handle simple chat interactions.
    """

    def __init__(self, model):
        self.model = model
    
    def process(self, state: State):
        """
        Process the state by generating a response based on the user input.
        
        Args:
            state (State): The current state of the chatbot, which includes user input.
        
        Returns:
            State: The updated state with the model's response.
        """
        return {"messages": self.model.invoke(state["messages"])}