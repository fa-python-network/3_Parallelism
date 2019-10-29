from multiprocessing import Pool, cpu_count

FILENAME = 'lorem.enc'


def encoder(b: bytes, code: bytes = b'qwertyuiop[]asdf') -> bytes:
    return bytes(a ^ b for a, b in zip(b, code))


if __name__ == '__main__':
    with open(FILENAME, 'rb') as file:
        to_encode = file.read()
    print(len(to_encode) % 16)
    to_encode += b' ' * (len(to_encode) % 16)

    processes_pool = Pool(cpu_count())
    blocks = [to_encode[i:i + 16] for i in range(0, len(to_encode), 16)]

    encoded = processes_pool.map(encoder, blocks)
    with open(FILENAME + '.enc', 'wb')as file:
        file.write(b''.join(encoded))
