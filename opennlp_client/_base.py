# opennlp_client/_base.py
import grpc
from typing import Optional

class OpenNLPConnectionError(Exception):
    pass

class BaseClient:
    def __init__(self, address: str, timeout: Optional[float] = 5.0):
        self.address = address
        self.channel = grpc.insecure_channel(address)
        try:
            grpc.channel_ready_future(self.channel).result(timeout=timeout)
        except Exception as e:
            raise OpenNLPConnectionError(f"Could not connect to {address}: {e}")

    def close(self):
        self.channel.close()
