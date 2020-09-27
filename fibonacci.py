def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


if __name__ == '__main__':
    f = fibonacci()
    for _ in range(10):
        print(next(f))
