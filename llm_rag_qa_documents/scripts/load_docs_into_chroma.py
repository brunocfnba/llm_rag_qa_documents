import sys
import os

sys.path.append(os.path.abspath(""))

from llm_rag_qa_documents.loaders.load_and_process_document import LoadAndProcessBase
from llm_rag_qa_documents.factory.chroma_factory import ChromadbFactory
from llm_rag_qa_documents.factory.logger_factory import loggerFactory

def load_chroma_script():
    """
    Load the documents retrieved from the directory into chromadb.
    """  
    chroma = ChromadbFactory("llm_rag_qa_documents/data/chromadb")
    docs_loader = LoadAndProcessBase("llm_rag_qa_documents/data/documents")
    logger = loggerFactory().get_logger(__name__)

    logger.info("Starting loading docs process")
    pages_loaded = docs_loader.load_directory()
    split_documents = docs_loader.split_document(pages_loaded)
    docs_ready = docs_loader.from_document_to_chroma_lists(split_documents)

    chroma.recreate_collection("docs_collection")
    chroma.collection_add("docs_collection", docs_ready)
    logger.info("Data added to 'docs_collection' collection")


if __name__ == "__main__":
    load_chroma_script()