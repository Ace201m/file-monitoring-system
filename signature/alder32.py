from zlib import adler32

BLOCK_SIZE = 256*1024*1024


def alderCheckSum(file_name):
    sum_value = 1
    with open(file_name, 'rb') as f:
        while True:
            data = f.read(BLOCK_SIZE)
            if not data:
                break
            sum_value = adler32(data, sum_value)
            if sum_value < 0:
                sum_value += 2**32
    return hex(sum_value)[2:10].zfill(8).lower()
