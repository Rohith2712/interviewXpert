from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.runnables.history import RunnableWithMessageHistory

def create_agent(llm, tools, prompt):
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor

def wrap_with_history(agent_executor, get_session_history):
    return RunnableWithMessageHistory(agent_executor, get_session_history, input_messages_key="input", history_messages_key="history")
