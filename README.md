# SQL Chatbot

This project is a SQL chatbot that interacts with users to answer questions about any database. It uses natural language processing to generate SQL queries based on user input and provides responses based on the database schema and query results.

## Features

- Natural language processing to understand user queries
- Generates SQL queries based on user input
- Provides natural language responses based on SQL query results
- Maintains conversation history for context-aware responses

## Requirements

- Python 3.8+
- Streamlit 1.25.0
- Langchain 0.1.9
- Langchain-community 0.0.22
- Langchain-core 0.1.25
- Langchain-openai 0.0.7
- MySQL Connector Python 8.3.1
- Groq 0.4.3
- Langchain-groq 0.0.2

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/dialectDB.git
    cd dialectDB
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your database credentials:
    ```
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_NAME=your_db_name
    DB_HOST=your_db_host
    DB_PORT=your_db_port
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run src/app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to interact with the chatbot.

## Project Structure

- [`src/app.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FDell%2FDesktop%2FdialectDB%2Fsrc%2Fapp.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\Dell\Desktop\dialectDB\src\app.py"): Main application file containing the chatbot logic.
- [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FDell%2FDesktop%2FdialectDB%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\Dell\Desktop\dialectDB\requirements.txt"): List of dependencies required for the project.
- [`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FDell%2FDesktop%2FdialectDB%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\Dell\Desktop\dialectDB\.env"): Environment file containing database credentials (not included in the repository).

## Functions

- [`database_connect`](command:_github.copilot.openSymbolFromReferences?%5B%22database_connect%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5CDell%5C%5CDesktop%5C%5CdialectDB%5C%5Csrc%5C%5Capp.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2FDell%2FDesktop%2FdialectDB%2Fsrc%2Fapp.py%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FDell%2FDesktop%2FdialectDB%2Fsrc%2Fapp.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A10%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition"): Connects to the SQL database using provided credentials.
- [`sql_chain_connect`](command:_github.copilot.openSymbolFromReferences?%5B%22sql_chain_connect%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5CDell%5C%5CDesktop%5C%5CdialectDB%5C%5Csrc%5C%5Capp.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2FDell%2FDesktop%2FdialectDB%2Fsrc%2Fapp.py%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FDell%2FDesktop%2FdialectDB%2Fsrc%2Fapp.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A20%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition"): Generates SQL queries based on user input and conversation history.
- [`response`](command:_github.copilot.openSymbolFromReferences?%5B%22response%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5CDell%5C%5CDesktop%5C%5CdialectDB%5C%5Csrc%5C%5Capp.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2FDell%2FDesktop%2FdialectDB%2Fsrc%2Fapp.py%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FDell%2FDesktop%2FdialectDB%2Fsrc%2Fapp.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A64%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition"): Generates natural language responses based on SQL query results.
