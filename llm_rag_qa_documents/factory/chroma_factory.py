import chromadb
from llm_rag_qa_documents.factory.logger_factory import loggerFactory

class ChromadbFactory():
    def __init__(self,
                 db_directory=None):
        """
        Initialize Chromadb

        :param db_directory: Path to generate the persistent db (default None).
        :type db_directory: String
        """
        self.db_directory = db_directory
        self.logger = loggerFactory().get_logger(__name__)

        if self.db_directory != None:
            self.chroma_client = chromadb.PersistentClient(path=self.db_directory)
        else:
            self.logger.error("No Persistent Directory Defined for ChromaDB")
            Exception("No Persistent Directory Defined for ChromaDB")

    def recreate_collection(self, collection_name):
        """
        Recreate a collection in case it already exists or create it case it's not there.

        :param collection_name: Name of the collection to be recreated
        :type collection_name: String
        """
        try:
            self.chroma_client.get_collection(name=collection_name)
            self.chroma_client.delete_collection(name=collection_name)
            self.chroma_client.create_collection(name=collection_name)
        except ValueError: 
            self.logger.info(f"Collection {collection_name} does not exist, creating")
            self.chroma_client.create_collection(name=collection_name)

    def collection_add(self, collection_name, chroma_dict):
        """
        Add content to a given collection.

        :param collection_name: Name of the collection
        :type collection_name: String
        :param chroma_dict: dictionary with the required structure and content to be added
        :type chroma_dict: Dict
        """
        try:
            collection = self.chroma_client.get_collection(name=collection_name)
            collection.add(ids=chroma_dict["ids"], documents=chroma_dict["contents"], metadatas=chroma_dict["metadatas"])
        except ValueError:
            self.logger.error(f"Collection {collection} does not exist")

    def collection_query(self, search_string, number_results, collection_name, metadata_filter=None):
        """
        Query a given collection.

        :param search_string: string to be searched for
        :type search_string: String
        :param number_results: how many results should be retrieved
        :type number_results: Integer
        :param collection_name: Name of the collection
        :type collection_name: String
        :param metadata_filter: "where clause" to be applied to the document metadata
        :type metadata_filter: Dict
        """
        try:
            collection = self.chroma_client.get_collection(name=collection_name)
            return collection.query(query_texts=search_string, include=["documents", "metadatas", "distances"], n_results=number_results, where=metadata_filter)
        except:
            self.logger.error("Unable to retrive data")