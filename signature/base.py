import hashlib


class BaseSignature:
    def __init__(self, path):
        self.file_path = path
        self.hash = 'EMPTY'

    def getSignature(self):
        with open(self.file_path, 'rb') as f:
            byte = f.read()
            self.hash = hashlib.sha512(byte).hexdigest()
        return self.hash
