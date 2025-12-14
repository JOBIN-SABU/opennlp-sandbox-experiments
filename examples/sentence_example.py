import grpc
from opennlp_client.sentence import SentenceServiceClient


def main():
    # Use the port your server actually started on
    channel = grpc.insecure_channel("localhost:7071")
    client = SentenceServiceClient(channel)

    text = "Hello world. This is a test sentence for OpenNLP."
    sentences = client.detect_sentences(text)

    print("Detected sentences:")
    for s in sentences:
        print("-", s)


if __name__ == "__main__":
    main()
