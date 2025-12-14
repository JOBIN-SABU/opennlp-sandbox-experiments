from opennlp_client import Tokenizer

t = Tokenizer("localhost:50051")
print(t.tokenize("This is a test sentence."))
t.close()
