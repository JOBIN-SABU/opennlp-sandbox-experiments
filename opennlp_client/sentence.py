import grpc
from opennlp_client.proto import opennlp_pb2, opennlp_pb2_grpc


class SentenceServiceClient:
    def __init__(self, channel):
        self.stub = opennlp_pb2_grpc.SentenceDetectorServiceStub(channel)

    def detect_sentences(self, text: str):
        """Send text to OpenNLP Sentence Detector gRPC service."""
        # Correct field name from proto: 'sentence'
        request = opennlp_pb2.SentDetectRequest(sentence=text)
        response = self.stub.sentDetect(request)
        return response.values  # because the server returns a StringList
