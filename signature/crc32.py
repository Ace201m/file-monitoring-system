import binascii


def crc32CheckSum(file_name):
    buf = open(file_name, 'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf
