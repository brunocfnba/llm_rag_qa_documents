
from langchain_community.document_loaders.directory import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class LoadAndProcessBase():

    def __init__(
        self,
        directory_path):
        self.directory_path = directory_path
        """
        Initialize the class.

        :param directory_path: the directory path to be searched for documents
        :type directory_path: String
        """  

    def load_directory(self):
        """
        Loads data from a directory into memory.
        """  
        loader = DirectoryLoader(self.directory_path)
        return loader.load()
    
    def split_document(self, document_pages):
        """
        Split the documents into chunks with some overlap.

        :param document_pages: a list with all the document pages loaded
        :type document_pages: List
        """  
        recursive_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        return recursive_splitter.split_documents(document_pages)

    def from_document_to_chroma_lists(self, split_document):
        """
        Format the split output into a dictionary to make it easier for chromadb ingestion.

        :param split_document: a list with all the documents split in chunks
        :type split_document: List
        """  
        ids_list = []
        docs_list = []
        metadata_list = []
        id = 1
        for i in split_document:
            ids_list.append(f"id{id}")
            docs_list.append(i.page_content)
            metadata_list.append(i.metadata)
            id = id+1

        chroma_lists = {}
        chroma_lists["ids"] = ids_list
        chroma_lists["contents"] = docs_list
        chroma_lists["metadatas"] = metadata_list
        return chroma_lists
