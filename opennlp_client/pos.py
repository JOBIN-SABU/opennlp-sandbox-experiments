# opennlp_client/pos.py
from typing import List
from ._base import BaseClient
from .proto import opennlp_pb2, opennlp_pb2_grpc

class PosTagger(BaseClient):
    def __init__(self, address: str):
        super().__init__(address)
        self.stub = opennlp_pb2_grpc.PosTaggerStub(self.channel)

    def tag(self, tokens: List[str]) -> List[str]:
        """
        tokens: list of tokens from tokenizer
        returns: list of POS tags in same order
        """
        # Edit message names as per opennlp.proto
        req = opennlp_pb2.PosTagRequest(tokens=tokens)
        resp = self.stub.Tag(req)   # RPC name might be 'Tag' or 'TagPOS' — update accordingly
        return list(resp.tags)
