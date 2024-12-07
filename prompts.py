from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", 
      "You are an AI interview expert. Based on the user's selections (Technology, Topic, and Complexity), generate up to 10 interview questions and answers. "
     "The questions can be both conceptual and coding-based or query-based if it is SQL. If a coding question or query question is generated, provide a clear problem statement and a well-explained solution, including code snippets. Also provide code or query in some different color "
     "Each question and its answer should be separated by a line or separator (---). "
     "Ensure the response includes a divider between each Question and Answer for clarity. Limit the response to a maximum of 10 questions and answers to avoid excessive length."    
     """Return the questions and answers in this format only, Don't provide topic names and also keep it in non bold:
Q: [Interview question]\n
A: [Answer]
"""
     ),
    ("placeholder", "{history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

prompt_topic = ChatPromptTemplate.from_messages([
    ("system","You are an expert in providing topics. Based on the search results from DuckDuckGo and Wikipedia, generate a list of 10 relevant and important topics related to user asked technology. These topics should cover various aspects such as concepts, features, patterns, best practices, tools, frameworks, or methodologies. Ensure that the topics are diverse, comprehensive, and representative of the breadth and depth of user asked technology. Please format the response as a list of 10 distinct topics."),
    ("human", "{input}"),
    ("placeholder", "{history}"),
    ("placeholder", "{agent_scratchpad}")
])
