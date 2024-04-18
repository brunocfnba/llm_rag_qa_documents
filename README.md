# Specific Documents trained Chatbot

This is a simple python code leveraging LLMs to answer questions about specific documents provided by you. It leverages Retrieval Augmented Generation (RAG) technique along with prompt engineering.

## Getting Started
1. Make sure you have Python Poetry installed and run the required poetry commands to get all the dependencies installed.
2. Add your own text files into `data/documents` directory (You need to create the `data` and `documents` directories).
3. I provided a sample `sample.env` that you need to rename to `.env` and add your APIKEY and other details to access your own watsonx.ai instance.
4. Run `poetry run python llm_rag_qa_documents/load_docs_into_chroma.py` - this will process your text files and add them to ChromaDB, a local vectorstore database.
5. Run `poetry run python llm_rag_qa_documents/main.py` - this will start a python panel local server and open a new browser with the chat bot interface.