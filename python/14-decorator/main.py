import time


def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Время исполнения {end - start}")
        print("Перехожу к другой функции.")
        return result

    return wrapper

@decorator
def load_file(seconds):
    print("Загружен какой то файл")
    time.sleep(2)

load_file(1)

@decorator
def multiply(a, b):
    print("Считаю чсила...")
    time.sleep(2)
    return a * b


print(multiply(5, 2))