# 🧠 MediMind – Your AI Health Companion

**MediMind** is an AI-powered chatbot that provides intelligent, context-aware answers to health-related questions using content from medical PDFs. It leverages **LangChain**, **FAISS**, and **LLaMA 2** running locally for private, fast, and helpful health conversations — right from your browser.

## 📁 Project Structure

```
healthcare-chatbot/
├─ app.py .............. Main Flask application
├─ app1.py ............. Vector store creation/setup script
├─ README.md ........... Project documentation
├─ requirements.txt .... Python dependencies
├─ data/
│  └─ Medical_book.pdf . Source medical reference document
└─ templates/
   └─ index.html ....... Frontend UI for chatting
```

## 🚀 Features

✅ Chat with a local AI about health topics

✅ Context-aware answers using Medical_book.pdf

✅ Works fully offline (no cloud LLMs)

✅ Powered by LLaMA 2 + FAISS + LangChain

✅ Lightweight web UI with Flask

## 🛠️ Setup Instructions

###### Step-by-Step to Run MediMind

1. **Create a virtual environment**

```
python -m venv myenv
```

2. Activate the environment

On Windows:

```
myenv\Scripts\activate
```

3. Download the LLaMA 2 model

- Visit: [LLaMA 2 GGML on Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)
- Download: `llama-2-7b-chat.ggmlv3.q4_1.bin`
- Place it in the project root directory.

4. Install dependencies

```
pip install -r requirements.txt
```

5. Create the vector store

```
python app1.py
```

6. Run the MediMind chatbot

```
python app.py
```

7. Use the chatbot

- Open your browser and go to `http://127.0.0.1:5000`
- Ask away!

## 💡 How MediMind Works

1. 🧾 User enters a health-related question.

2. 🔍 FAISS retrieves relevant content chunks from the medical PDF.

3. 🧠 LangChain passes context + question to the LLaMA 2 model.

4. 💬 The model replies with a helpful, grounded answer.

## 📸 Output Screenshots

- Screenshot 1: Homepage UI
  ![HomePage UI](<https://ik.imagekit.io/pzzgzwooz/Screenshot%20(14).png?updatedAt=1752578938817>)
- Screenshot 2: Sample query & response
  ![Sample query and response](<https://ik.imagekit.io/pzzgzwooz/Screenshot%20(15).png?updatedAt=1752578962056>)

## 🔮 Future Improvements

- 🔐 Add user authentication
- 💬 Improve chatbot UI with real-time bubbles
- 📚 Support multiple PDFs and document uploads
- 🐳 Dockerize for easy deployment
- ☁️ Optional cloud deployment on Render or Hugging Face Spaces

## 👩‍⚕️ Tagline

"MediMind – Let knowledge care for you."
