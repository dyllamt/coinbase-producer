import kafka
import pytest


class KafkaMockProducer(kafka.KafkaProducer):

    def __init__(self):
        self.messages = []  # collects messages sent by producer

    async def send(self, topic: str, message: str):
        self.messages.append(message)


@pytest.fixture()
def kafka_producer():
    return KafkaMockProducer()
