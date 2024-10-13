from embedding_model.sentencetransformer import Embedder
model_list = [
    "all-MiniLM-L12-v2",
    "nvidia/NV-Embed-v2",
    ]
model_name = model_list[0]
local_path = r"C:\LlamaSensei\app\pretrained_model\all-MiniLM-L12-v2"
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
main()