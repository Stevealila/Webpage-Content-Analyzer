# ...................................Uses OpenAI models.............................

from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import streamlit as st

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


def load_docs(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    return docs


def create_vectorestore_retriever(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = FAISS.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever()
    return retriever


def create_prompt_template():
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, say that you don't know."
        "\n\n"
        "{context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    return prompt


def retrieve_documents(llm, prompt_template, retriever):
    question_answer_chain = create_stuff_documents_chain(llm, prompt_template)
    chain = create_retrieval_chain(retriever, question_answer_chain)
    return chain

def filter_answer(chain, question):
    result = chain.invoke({"input": question})
    best_answer = result.get('answer')
    return best_answer

def analyze_webpage_content(url, question):
    docs = load_docs(url)
    llm = ChatOpenAI(model="gpt-4o")
    prompt_template = create_prompt_template()
    retriever = create_vectorestore_retriever(docs)
    chain = retrieve_documents(llm, prompt_template, retriever)
    result = filter_answer(chain, question)
    return result


# Streamlit UI
st.title("Webpage Content Analyzer")

url = st.text_input("Enter the webpage URL:")
question = st.text_input("Enter your question:")

if st.button("Analyze"):
    with st.spinner("Analyzing..."):
        result = analyze_webpage_content(url, question)
        st.success("Analysis complete!")
        st.write(result)
