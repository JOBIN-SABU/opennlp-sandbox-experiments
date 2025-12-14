# opennlp_client/tokenizer.py
from typing import List
from ._base import BaseClient
from .proto import opennlp_pb2, opennlp_pb2_grpc

class Tokenizer(BaseClient):
    def __init__(self, address: str):
        super().__init__(address)
        # This class name must exist in the generated *_pb2_grpc.py
        self.stub = opennlp_pb2_grpc.TokenizerStub(self.channel)

    def tokenize(self, text: str) -> List[str]:
        """
        Returns a list of tokens.
        NOTE: adjust TokenizeRequest / Tokenize response field names to match the proto.
        """
        # ---- Edit these names to match the actual proto messages ----
        req = opennlp_pb2.TokenizeRequest(text=text)      # <-- name likely here; update if different
        resp = self.stub.Tokenize(req)                    # <-- RPC name might be Tokenize or TokenizeText
        # assume response has repeated field `tokens`
        return list(resp.tokens)
