from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.utilities import SQLDatabase
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

def database_connect(
    user: str,
    password: str,
    database: str,
    host: str = "localhost",
    port: int = 3306,
) -> SQLDatabase:
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)

def sql_chain_connect(db):
    template = """"
        You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
        Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account.

        <SCHEMA>{schema}</SCHEMA>

        Conversation History: {chat_history}

        Your task is to write only the SQL query needed to answer the user's question. Do not include any other text or explanations in your response. Avoid wrapping the SQL query in backticks or any other formatting.

        Examples:
        1. Question: What are the top 5 YouTubers with the highest number of subscribers?
        SQL Query: SELECT YouTuberName, Subscribers FROM YouTubers ORDER BY Subscribers DESC LIMIT 5;

        2. Question: How many views did the most recent video by 'pewdiepie' receive?
        SQL Query: SELECT Views FROM Videos WHERE YouTuberName = 'pewdiepie' ORDER BY UploadDate DESC LIMIT 1;

        3. Question: List the titles of the top 3 videos with the highest number of likes.
        SQL Query: SELECT VideoTitle, Likes FROM Videos ORDER BY Likes DESC LIMIT 3;

        4. Question: Find the average number of views per video for each YouTuber who has more than 1 million subscribers.
        SQL Query: SELECT YouTuberName, AVG(Views) AS AvgViews FROM Videos JOIN YouTubers ON Videos.YouTuberID = YouTubers.YouTuberID WHERE Subscribers > 1000000 GROUP BY YouTuberName;

        Your turn:

        Question: {question}
        SQL Query:
    """

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0)

    def get_schema(_):
        return db.get_table_info()
    
    return (
        RunnablePassthrough.assign(schema=get_schema)
        | prompt
        | llm
        | StrOutputParser()
    )

def response(user_query: str, db: SQLDatabase, chat_history: list):
    sql_chain = sql_chain_connect(db)

    template = """"
        You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
        Based on the table schema below, question, sql query, and sql response, write a natural language response.
        <SCHEMA>{schema}</SCHEMA>

        Conversation History: {chat_history}
        SQL Query: <SQL>{query}</SQL>
        User question: {question}
        SQL Response: {response}
    """
    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0)

    chain = (
        RunnablePassthrough.assign(query=sql_chain).assign(
            chema=lambda _: db.get_table_info(),
            response=lambda vars: db.run(vars["query"]),
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain.invoke({
        "question": user_query,
        "chat_history": chat_history
    })

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        AIMessage(content="Hello! I'm Dwight. I can help you with your MySQL queries. Connect to the database to get started.")
    ]

load_dotenv()

st.set_page_config(page_title="dialectDB", page_icon="🎯")

st.title("Chat with dwight 🚀")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a chatbot that can help you with your MySOL queries. Connect to the database to get started.")

    st.text_input("Host", value="localhost", key="Host")   
    st.text_input("Port", value="3306", key="Port")
    st.text_input("User", value="root", key="User")
    st.text_input("Password", type="password", value="password", key="Password")
    st.text_input("Database", value="schrutes", key="Database")  

    if st.button("Connect"):
        with st.spinner("Connecting to database..."):
            user = st.session_state["User"]
            password = st.session_state["Password"]
            database = st.session_state["Database"]
            host = st.session_state["Host"]
            port = int(st.session_state["Port"])
            db = database_connect(user, password, database, host, port)
            st.session_state["db"] = db
            st.success("Connected to database.")

for message in st.session_state["chat_history"]:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

user_query = st.chat_input("Type a message...")
if user_query is not None and user_query.strip() != "":
    st.session_state["chat_history"].append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        # response = "I'm sorry, I don't understand that."
        response = response(user_query, st.session_state["db"], st.session_state["chat_history"])
        st.markdown(response)

    st.session_state["chat_history"].append(AIMessage(content=response))
