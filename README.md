# Agentic Chatbot with LangGraph and Streamlit

This project is an end-to-end implementation of a conversational AI agent using LangGraph. The agent is capable of holding stateful conversations and is presented through a user-friendly web interface built with Streamlit.

## 🚀 Overview

LangGraph is a powerful library for building stateful, multi-actor applications with Large Language Models (LLMs). It extends the LangChain Expression Language to enable the creation of cyclical graphs, which are essential for building robust agents that can loop, make decisions, and use tools.

This chatbot demonstrates a fundamental agentic loop where the agent can:
1.  Receive user input.
2.  Call an LLM to decide the next action.
3.  Execute tools (if any are defined).
4.  Generate a response.
5.  Maintain the conversation state throughout the interaction.

The frontend is built with Streamlit, providing a simple and interactive UI for chatting with the agent.

## ✨ Features

*   **Stateful Conversations:** The agent remembers the context of the conversation across multiple turns.
*   **Agentic Logic:** Utilizes a state graph to manage complex, multi-step interactions and decision-making.
*   **Interactive UI:** A clean and simple web interface powered by Streamlit for real-time interaction.
*   **Cyclical Computation:** The graph structure allows for loops, enabling more complex and natural conversational flows than simple chains.
*   **Extensible:** The architecture makes it easy to add new tools and capabilities to the agent.

## 🛠️ Tech Stack

*   **Backend:** Python
*   **LLM Orchestration:** [LangChain](https://www.langchain.com/), [LangGraph](https://python.langchain.com/docs/langgraph)
*   **Frontend:** [Streamlit](https://streamlit.io/)
*   **LLM:** Configurable to use models like OpenAI's GPT, Google's Gemini, or other compatible LLMs.

## 📂 Project Structure

A recommended structure for this project:

```
agentic-chatbot-langgraph/
├── .gitignore
├── README.md
├── requirements.txt
├── .env                 # For API keys and environment variables
├── app.py               # Main Streamlit application
└── src/
    ├── __init__.py
    └── agent_graph.py   # LangGraph state graph definition and agent logic
```

## ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ChidambaraRaju/agentic-chatbot-langgraph.git
    cd agentic-chatbot-langgraph
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your necessary API keys.
    ```
    # Example for OpenAI
    OPENAI_API_KEY="your-openai-api-key-here"
    ```

## ▶️ How to Run

Once the setup is complete, run the Streamlit application from your terminal:

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your web browser to start chatting with your agent.

## 🤖 How It Works: The LangGraph Agent

The core of this chatbot is the state graph defined in `src/agent_graph.py`. A state graph is composed of **nodes** and **edges**.

1.  **State:** A central `State` object (e.g., a `TypedDict`) is defined to pass information between nodes. This typically includes the conversation history, user input, and any intermediate results.

2.  **Nodes:** Each node is a Python function or a LangChain Runnable that performs a specific task. Common nodes in an agentic graph include one to call the LLM, one to execute tools, and one to format the final response.

3.  **Edges:** Edges connect the nodes and direct the flow of logic. **Conditional edges** are particularly important, as they allow the graph to decide which node to visit next based on the current state (e.g., "did the LLM decide to use a tool or respond directly?").

The graph begins at an `ENTRYPOINT`, processes the input through its nodes and edges, and continues until it generates a response for the user, updating its state along the way.