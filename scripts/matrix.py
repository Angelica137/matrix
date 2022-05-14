class Matrix:

    def __init__(self, numbers: str) -> str:
        self.numbers = numbers

    def rows(self):
        return self.numbers.split("\n")
