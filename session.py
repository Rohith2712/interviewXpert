import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

if "store" not in st.session_state:
    st.session_state.store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in st.session_state.store:
        st.session_state.store[session_id] = ChatMessageHistory()
    return st.session_state.store[session_id]

def update_topics(technology):
    if technology == '.NET':
        st.session_state.topics = [
            'ASP.NET Core', 'Entity Framework', 'LINQ', 'MVC Architecture', 'Dependency Injection', 
            'Authentication and Authorization', 'Web API Development', 'Asynchronous Programming', 
            'Design Patterns in .net', 'Caching Strategies', 'Multithreading'
        ]
    elif technology == 'C#':
        st.session_state.topics = [
            'OOP Concepts', 'LINQ', 'Delegates and Events', 'Async/Await', 'Exception Handling', 
            'Generics', 'Data Structures', 'Garbage Collection', 'Lambda Expressions', 'Memory Management and Garbage Collection', 
            'Serialization/Deserialization'
        ]
    elif technology == 'Angular':
        st.session_state.topics = [
            'Components and Directives', 'Services and Dependency Injection', 'Routing', 'RxJS', 
            'Forms (Reactive and Template-driven)', 'NgModules', 'HTTP Client', 'Angular CLI', 
            'State Management (NgRx)', 'Pipes', 'Angular Universal (SSR)', 'Testing Angular Applications'
        ]
    elif technology == 'SQL':
        st.session_state.topics = [
            'Joins', 'Indexes', 'Stored Procedures', 'Triggers', 'Common Table Expressions', 
            'Transactions', 'Views', 'SQL Injection', 'Database Design', 'Backup and Recovery', 
            'Subqueries', 'Query Performance Tuning'
        ]
    elif technology == 'Java':
        st.session_state.topics = [
            'Variables and Data Types', 'Control Flow Statements (if, else, switch)', 'Loops (for, while, do-while)', 
            'Arrays in Java', 'String Manipulation', 'Methods and Functions', 'Object-Oriented Programming (OOP) Concepts', 
            'Classes and Objects', 'Constructors', 'Access Modifiers', 'Exception Handling (try-catch)', 'Basic Input/Output in Java'
        ]
    elif technology == 'Agile':
        st.session_state.topics = [
            'Introduction to Agile Methodology', 'Agile vs. Waterfall Methodology', 'Scrum Framework', 'Kanban Methodology', 
            'User Stories and Acceptance Criteria', 'Agile Estimation (Story Points, Planning Poker)', 'Sprint Planning and Execution', 
            'Daily Standups and Sprint Reviews', 'Role of Scrum Master', 'Role of Product Owner', 'Agile Retrospectives', 
            'Agile Testing and Continuous Integration'
        ]
