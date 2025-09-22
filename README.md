# 📊 Chat with SQL Database (LangChain + Streamlit + Groq)

This project is a **Streamlit app** that allows you to chat with your SQL database using **LangChain Agents** and the **Groq LLM API**.  
You can ask natural language queries like:

- *“Show me all records in the STUDENT table”*  
- *“What is the average grade of students in AI?”*  

The agent converts your question → SQL query → executes on the database → shows results back in Streamlit.

---

## 🚀 Features
- Connects to any SQLite database.  
- Uses **LangChain SQLDatabaseToolkit** to expose DB schema.  
- Integrates with **Groq LLM** for query reasoning.  
- Conversational memory with `st.session_state`.  
- Restricts the agent to only real DB tables (avoids hallucinations).  

---

