from abc import ABC, abstractmethod
import json


class SerializationInterface(ABC):
    @abstractmethod
    def serialize(self, file_name, data):
        pass

    @abstractmethod
    def deserialize(self, file_name):
        pass


class SerialToBin(SerializationInterface):
    def serialize(self, file_name, data: str):
        with open(file_name, 'wb') as fh:
            fh.write(data.encode())

    def deserialize(self, file_name):
        with open(file_name, 'rb') as fh:
            return fh.read().decode()


class SerialToJson(SerializationInterface):
    def serialize(self, file_name, data):
        with open(file_name, 'w', encoding='utf-8') as fh:
            json.dump(data, fh)

    def deserialize(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as fh:
            return json.load(fh)


if __name__ == '__main__':
    pass
