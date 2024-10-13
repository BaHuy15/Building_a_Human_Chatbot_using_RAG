from abc import ABC, abstractmethod


class BaseVectorDB(ABC):
    """Abstract base class for vector databases."""
    
    def __init__(self, collection_name, vector_size, distance_metric="Cosine"):
        self.collection_name = collection_name
        self.vector_size = vector_size
        self.distance_metric = distance_metric

    @abstractmethod
    def create_collection(self):
        """Abstract method to create a collection in the vector database."""
        pass

    @abstractmethod
    def insert_vectors(self, vectors, payloads):
        """Abstract method to insert vectors into the collection."""
        pass

    @abstractmethod
    def search_vectors(self, query_vector, top_k=3):
        """Abstract method to search for the nearest vectors to a query vector."""
        pass

    @abstractmethod
    def delete_collection(self):
        """Abstract method to delete the collection."""
        pass


