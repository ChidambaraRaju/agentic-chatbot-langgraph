import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.

    """

    ##Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    user_message = st.chat_input("Enter your message:")
    
    if not user_message:
        st.warning("Please enter a message to continue.")
        return
    
    if user_message:
        obj_llm_config = GroqLLM(user_controls_input=user_input)
        model = obj_llm_config.get_groq_llm()
        if not model:
            st.error("Error: Failed to configure the LLM model.")
            return
        
        use_case = user_input.get("selected_usecase")
        if not use_case:
            st.error("Error: No use case selected.")
            return
        
        ## Build the graph based on the selected use case
        graph_builder=GraphBuilder(model)
        try:
                 graph=graph_builder.setup_graph(use_case)
                 print(user_message)
                 DisplayResultStreamlit(use_case,graph,user_message).display_result_on_ui()
        except Exception as e:
                 st.error(f"Error: Graph set up failed- {e}")
                 return

        except Exception as e:
             st.error(f"Error: Graph set up failed- {e}")
             return  