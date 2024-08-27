from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.utilities import SQLDatabase
import streamlit as st

def database_connect(
    user: str,
    password: str,
    database: str,
    host: str = "localhost",
    port: int = 3306,
) -> SQLDatabase:
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)



if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        AIMessage(content="Hello! I'm Dwight. I can help you with your MySOL queries. Connect to the database to get started.")
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
        response = "I'm sorry, I don't understand that."
        st.markdown(response)

    st.session_state["chat_history"].append(AIMessage(content=response))
