from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
class GraphBuilder:
    def __init__(self,model):
        self.model = model
        self.graph = StateGraph(State)
        
    def basic_chatbot_graph_builder(self):
        """
        Builds a basic chatbot graph with a single state for the user input and a response from the model.
        """
        self.chatbot = BasicChatbotNode(self.model)
        self.graph.add_node("chatbot", self.chatbot.process)
        self.graph.add_edge(START, "chatbot")
        self.graph.add_edge("chatbot", END)
        
    def setup_graph(self, use_case):
        """
        Sets up the graph based on the selected use case.
        
        Args:
            use_case (str): The selected use case to determine the graph structure.
        """
        if use_case == "Basic Chatbot":
            self.basic_chatbot_graph_builder()
        
            return self.graph.compile()