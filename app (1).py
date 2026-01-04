import os
import gradio as gr

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5

)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an enthusiastic high school student passionate about science and exploration. You spend most of your free time conducting experiments, reading scientific journals, and dreaming of a future as a renowned scientist. Your knowledge spans various scientific fields, and you love sharing fun facts and engaging in lively discussions about the latest discoveries."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)
def respond(message, history):
    response = chatbot.invoke(
        {"input": message},
        config={"configurable": {"session_id": "default"}}
    )
    return response.content
demo = gr.ChatInterface(
    fn=respond,
    examples=[
        "How are you doing?",
        "What are your interests?",
        "Which places do you like to visit?"
    ],
    title="Generative AI Chatbot",
    description="Powered by OpenAI + LangChain"
)
demo.launch()
