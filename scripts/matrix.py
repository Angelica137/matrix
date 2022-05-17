class Matrix:

    def __init__(self, numbers: str) -> str:
        self.numbers = numbers

    def rows(self):
        return self.numbers.split("\n")

    def columns(self):
        columns = []
        i = 0
        while i < len(self.rows()[0]):
            column = ""
            for row in self.rows():
                column += row[i] + " "
            i += 2
            columns.append(column[:-1])
        return columns
