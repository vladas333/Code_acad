def add(x: int, y: int) -> int:
    return x + y


def sub(x: int, y: int) -> int:
    return x - y


def prod(x: int, y: int) -> int:
    return x * y


def div(x: int, y: int) -> int:
    return x // y


print(f"I am i some file: {__name__} .py")

# check python code is it run

if __name__ == "__main__":
    a = 500
    b = 1500
    result = prod(a, b)
    print(result)
