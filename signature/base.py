from signature import crc32, alder32


class BaseSignature:
    def __init__(self, path):
        self.file_path = path
        self.hash = 'EMPTY'

    def getSignature(self):
        alderCheckSum = alder32.alderCheckSum(self.file_path)
        crcCheckSum = crc32.crc32CheckSum(self.file_path)
        self.hash = alderCheckSum+'#'+crcCheckSum
        return self.hash
