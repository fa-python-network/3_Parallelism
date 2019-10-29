from multiprocessing import Pool, cpu_count

CODE = b'qwertyuiop[]asdf'


def encoder(b: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(b, CODE))


if __name__ == '__main__':
    filename = input('Input filename ')
    CODE = input('Input 16-symbols code phrase ')
    while len(CODE) != 16:
        CODE = input('Input 16-symbols code phrase ')
    CODE = CODE.encode()
    with open(filename, 'rb') as file:
        to_encode = file.read()
    to_add = 16 - (len(to_encode) % 16)
    to_encode += b' ' * (to_add if to_add != 16 else 0)

    processes_pool = Pool(cpu_count())
    blocks = [to_encode[i:i + 16] for i in range(0, len(to_encode), 16)]

    encoded = processes_pool.map(encoder, blocks)
    with open(filename + '.enc', 'wb')as file:
        file.write(b''.join(encoded))
