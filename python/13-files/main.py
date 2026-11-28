
file = open('data.txt', 'r')
try:
    print(file.read())
finally:
    file.close()

with open('data.txt', 'r') as data:
    print(data.read())

class FileOpener:
    def __init__(self, file_path: str, mode: str):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.data = open(self.file_path, self.mode)
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.data.close()
        print(f"Ошибка внути with - {exc_type}, текст ошибки - {exc_val}")
        return True

with FileOpener('data.txt', 'r') as data:
    print(data.read())
    print(10/0)