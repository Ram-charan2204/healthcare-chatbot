import logging
from flask import Flask, render_template, request, jsonify
from langchain_core.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import CTransformers

logging.basicConfig(level=logging.DEBUG)

DB_FAISS_PATH = "vectorstores/db_faiss"

custom_prompt_template = """use the following pieces of information to answer the user's question.
if you don't know the answer, please just say that you don't know the answer, don't try to make up an answer.
context : {context}
question: {question}
Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    """Prompt template for QA retrieval for each vector store"""
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])
    return prompt

def load_llm():
    logging.info("Loading LLM...")
    llm = CTransformers(
        model='llama-2-7b-chat.ggmlv3.q4_0.bin',
        model_type='llama',
        max_new_tokens=512,
        temperature=0.5
    )
    logging.info("LLM loaded successfully.")
    return llm

def load_vector_store():
    logging.info("Loading vector store...")
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    logging.info("Vector store loaded successfully.")
    return db

def retrieval_qa_chain(llm, prompt, db):
    logging.info("Setting up RetrievalQA chain...")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=db.as_retriever(search_kwargs={'k': 2}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt}
    )
    logging.info("RetrievalQA chain set up successfully.")
    return qa_chain

def qa_bot():
    try:
        db = load_vector_store()
        llm = load_llm()
        qa_prompt = set_custom_prompt()
        qa = retrieval_qa_chain(llm, qa_prompt, db)
        return qa
    except Exception as e:
        logging.error(f"Error in qa_bot: {e}")
        raise e

qa = qa_bot()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('user_input')
    if user_input:
        result = qa({"query": user_input})
        response = result['result']
    else:
        response = "Please enter a valid query."
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
