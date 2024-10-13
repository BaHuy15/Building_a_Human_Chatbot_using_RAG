from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, PointStruct
import numpy as np
from Database.base import BaseVectorDB

class QdrantVectorDB(BaseVectorDB):
    def __init__(self, host="localhost", port=6333, collection_name="my_collection", vector_size=512, distance_metric="Cosine"):
        """
        Initialize the Qdrant client and set up a collection.

        :param host: Qdrant server host, default is localhost.
        :param port: Qdrant server port, default is 6333.
        :param collection_name: Name of the collection to create/use.
        :param vector_size: Dimension of the vector embeddings.
        :param distance_metric: Distance metric for similarity search (Cosine, Euclid, Dot).
        """
        self.collection_name = collection_name
        self.vector_size = vector_size
        self.client = QdrantClient(host=host, port=port)

        # Create or recreate the collection
        self.create_collection(distance_metric)

    def create_collection(self, distance_metric):
        """Creates or recreates the collection in Qdrant."""
        try:
            self.client.recreate_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=self.vector_size, distance=distance_metric)
            )
            print(f"Collection '{self.collection_name}' created with vector size {self.vector_size} and {distance_metric} distance metric.")
        except Exception as e:
            print(f"Error creating collection: {e}")

    def insert_vectors(self, vectors, payloads):
        """
        Inserts vectors into the collection.

        :param vectors: List of vectors to insert.
        :param payloads: List of metadata associated with each vector (must match the size of vectors).
        """
        try:
            points = [
                PointStruct(id=idx, vector=vector, payload=payload)
                for idx, (vector, payload) in enumerate(zip(vectors, payloads))
            ]
            self.client.upsert(collection_name=self.collection_name, points=points)
            print(f"Inserted {len(vectors)} vectors into {self.collection_name}.")
        except Exception as e:
            print(f"Error inserting vectors: {e}")

    def search_vectors(self, query_vector, top_k=3):
        """
        Searches for the nearest vectors to the query vector.

        :param query_vector: The vector to search for similarity.
        :param top_k: Number of top similar results to return.
        :return: Search results from Qdrant.
        """
        try:
            search_result = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                limit=top_k
            )
            return search_result
        except Exception as e:
            print(f"Error searching vectors: {e}")
            return []

    def delete_collection(self):
        """Deletes the current collection."""
        try:
            self.client.delete_collection(self.collection_name)
            print(f"Collection '{self.collection_name}' deleted.")
        except Exception as e:
            print(f"Error deleting collection: {e}")


# Utility functions for generating random vectors (can be replaced with actual embeddings)
def generate_random_vectors(num_vectors, vector_size):
    """
    Generates random vectors for demonstration.

    :param num_vectors: Number of vectors to generate.
    :param vector_size: Dimension of each vector.
    :return: A list of randomly generated vectors.
    """
    return [np.random.rand(vector_size).tolist() for _ in range(num_vectors)]


def generate_payloads(num_vectors):
    """
    Generates dummy payloads for the vectors.

    :param num_vectors: Number of payloads to generate.
    :return: A list of dictionaries representing payloads.
    """
    return [{"id": i, "description": f"Item {i}"} for i in range(num_vectors)]


# Example of usage
if __name__ == "__main__":
    # Initialize Qdrant Vector DB
    qdrant_db = QdrantVectorDB(collection_name="scalable_collection", vector_size=512, distance_metric="Cosine")

    # Generate and insert vectors with metadata
    num_vectors = 10
    vectors = generate_random_vectors(num_vectors, vector_size=512)
    payloads = generate_payloads(num_vectors)
    qdrant_db.insert_vectors(vectors, payloads)

    # Example query vector (normally you'd use an actual embedding)
    query_vector = np.random.rand(512).tolist()

    # Search for similar vectors
    results = qdrant_db.search_vectors(query_vector, top_k=5)
    for result in results:
        print(f"ID: {result.id}, Score: {result.score}, Metadata: {result.payload}")

    # Optional: Delete the collection (for cleanup)
    # qdrant_db.delete_collection()
