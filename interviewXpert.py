import streamlit as st
from config import *
from tools import tools, llm
from prompts import prompt, prompt_topic
from agent import create_agent, wrap_with_history
from session import update_topics, get_session_history

st.set_page_config(page_title="InterviewXpert - Interview Question Generator")
st.title("InterviewXpert")

if "topics" not in st.session_state:
    st.session_state.topics = ['None']

technologies = ['.NET', 'C#', 'Angular', 'SQL', 'Java', 'Agile']
complexities = ['Basic', 'Intermediate', 'Advanced']

technology = st.selectbox("Select Technology", technologies)
update_topics(technology)
st.session_state.topics.insert(0, 'None')
topic = st.selectbox("Select Topic (optional)", st.session_state.topics)
complexity = st.selectbox("Select Complexity", complexities)

agent_executor = create_agent(llm, tools, prompt)
agent_with_history = wrap_with_history(agent_executor, get_session_history)

def ensure_separators(response):
    question_answer_pairs = response.split("\n---\n")
    filtered_response = "\n---\n".join([pair.strip() for pair in question_answer_pairs if pair.strip()])
    max_output_length = 5000  
    if len(filtered_response) > max_output_length:
        filtered_response = filtered_response[:max_output_length] + "\n[Output truncated due to length]"
    return filtered_response

def generate_questions(technology, topic, complexity):
    if topic != 'None':
        query = f"Generate {complexity} interview questions and answers for {technology} on the topic of {topic}."
    else:
        agent_executor_topic = create_agent(llm, tools, prompt_topic)
        agent_with_history_topic = wrap_with_history(agent_executor_topic, get_session_history)
        query = f"Get top 10 {complexity} topics from DuckDuckGo search and Wikipedia for {technology} and Generate interview questions and answers for {technology} on those topics."
        topics = agent_with_history_topic.invoke({"input": query}, config={"configurable": {"session_id": "sess1"}})["output"]
        query = f"Generate {complexity} interview questions and answers for {technology} on the topic of {topics}."
    result = agent_with_history.invoke({"input": query}, config={"configurable": {"session_id": "sess1"}})
    return result["output"]

btn = st.button("Generate Interview Questions")

if btn:
    with st.spinner("Generating... please wait!"):
        answer = generate_questions(technology, topic, complexity)
        st.write(answer)
