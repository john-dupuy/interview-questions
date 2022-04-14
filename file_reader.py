class Reader:

    def __init__(self, path):
        self.file = open(path, "r")

    def __enter__(self):
        return self.file

    def print_content(self):
        lines = '- ' * 25
        print(f'{lines}\n{self.file.read()}\n{lines}')


with Reader('/home/x/pf.sh') as reader:
    reader.print_content()
