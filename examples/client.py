import grpc
from opennlp_client.proto import opennlp_pb2, opennlp_pb2_grpc

def main():
    # Connect to the running OpenNLP gRPC server
    channel = grpc.insecure_channel("localhost:50051")
    stub = opennlp_pb2_grpc.OpenNLPStub(channel)

    # Example: tokenize
    request = opennlp_pb2.TokenizerRequest(text="Hello world, this is OpenNLP.")
    response = stub.Tokenize(request)

    print("Tokens:", response.tokens)

if __name__ == "__main__":
    main()
