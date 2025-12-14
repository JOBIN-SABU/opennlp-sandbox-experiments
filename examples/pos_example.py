from opennlp_client import Tokenizer, PosTagger

tok = Tokenizer("localhost:50051")
tokens = tok.tokenize("Open the pod bay doors, HAL.")
print("Tokens:", tokens)

pos = PosTagger("localhost:50051")
print("POS:", pos.tag(tokens))
tok.close(); pos.close()
