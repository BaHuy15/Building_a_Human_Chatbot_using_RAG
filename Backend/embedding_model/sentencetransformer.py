from typing import List

import torch
from sentence_transformers import SentenceTransformer
import os
from embedding_model.base import Base
model_list = [
    "all-MiniLM-L12-v2",
    "nvidia/NV-Embed-v2",
    ]
model_name = model_list[0]
local_path = r"C:\LlamaSensei\app\pretrained_model\all-MiniLM-L12-v2"

class Embedder(Base):
    def __init__(self, model_name=model_name,local_path=local_path):
        device = "cuda" if torch.cuda.is_available() else "cpu"

        if len(os.listdir(local_path))==0:
            self.model = SentenceTransformer(model_name, trust_remote_code=True).to(device)
            self.model.save(local_path)
        else:
            self.model = SentenceTransformer(local_path).to(device)

    def encode(self, doc):
        return self.model.encode(doc)

    def encode_queries(self, chunks: List[tuple], top_chunks: int = None) -> List[tuple]:
        pass

def main():
    model_name = model_list[0]
    local_path = r"C:\LlamaSensei\app\pretrained_model\all-MiniLM-L12-v2"
    embedder = Embedder(model_name=model_name, local_path=local_path)
    sentences = [
                ("The weather is lovely today.",
                "It's so sunny outside!",)
                # "He drove to the stadium.",
            ]
    output_text = embedder.encode(sentences)
    print(output_text)
   
    # model = SentenceTransformer(model_name, trust_remote_code=True).to(device)  
    # model.save(r'C:\LlamaSensei\app\pretrained_model') 
    # output_text = model.encode(sentences)
    # print(output_text)

main()
    
