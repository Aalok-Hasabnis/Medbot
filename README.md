# 🩺 Medbot

A RAG-based medical chatbot that provides accurate information by retrieving content from medical documents using LangChain, Google Gemini, Pinecone, and Hugging Face embeddings.

## ✨ Features

- 🔍 Processes complex medical queries
- 📚 Retrieves relevant medical information from PDFs
- 🔄 Maintains conversation context
- 📱 Clean, responsive interface

## 🔧 Tech Stack

- **Backend**: Flask, Python
- **AI**: Google Gemini via `langchain_google_genai`
- **Vector DB**: Pinecone
- **Embeddings**: Hugging Face
- **Frontend**: HTML/CSS
- **Data**: Medical PDFs

## 📁 Structure

```
Medbot/
├── Data/                     # Medical PDF documents
├── Gen_Ai_Project.egg-info/  # Package information
├── research/                 # Research files
├── src/                      # Source code
├── static/                   # CSS, JS, images
├── templates/                # HTML templates
├── .env                      # Environment variables
├── .gitignore                # Git ignore file
├── app.py                    # Main Flask app
├── LICENSE                   # MIT license
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies
├── setup.py                  # Package setup file
├── store_index.py            # Vector store indexing
├── template.py               # Template utilities
└── test.py                   # Test scripts
```

## 🚀 Setup

1. **Clone repo**
   ```bash
   git clone https://github.com/Aalok-Hasabnis/Medbot.git
   cd Medbot
   ```

2. **Create environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # (Windows: venv\Scripts\activate)
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure .env file**
   ```
   PINECONE_API_KEY=your_key
   GOOGLE_API_KEY=your_key
   ```

5. **Run**
   ```bash
   python app.py
   ```
