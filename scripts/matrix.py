class Matrix:

    def __init__(self, matrix_string: str) -> str:
        self.matrix_string = matrix_string

    def rows(self) -> list:
        """
        Returns a list with the rows in the matrix
        """
        return self.matrix_string.split("\n")

    def row(self, row_number: int) -> list:
        """
        Returns the row requested by row_number
        """
        single_row = self.rows()[row_number - 1].split(" ")
        for i in range(len(single_row)):
            single_row[i] = int(single_row[i])
        return single_row

    def columns(self) -> list:
        """
        Returns a list with the columns in th ematrix
        """
        columns = []
        i = 0
        while i < len(self.rows()[0]):
            column = ""
            for row in self.rows():
                column += row[i] + " "
            i += 2
            columns.append(column[:-1])
        return columns


r = ['1']
for i in range(len(r)):
    r[i] = int(r[i])
print(r)
print('this is r')


m = Matrix("1 2 3\n4 5 6")

r = m.rows()[2 - 1].split(" ")
print(r)
for char in r:
    char = int(char)
print(r)


o = '1'
o = int(o)
print(o)

o = ['1']
o[0] = int(o[0])
print(o)
