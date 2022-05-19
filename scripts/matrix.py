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
        Returns a list with the columns in the matrix
        """
        columns = []
        rows = []
        for row in self.rows():
            rows.append(row.split(" "))
        i = 0
        while i < len(rows[0]):
            column = []
            for row in rows:
                column.append(row[i])
            columns.append(column)
            i += 1
        return columns

    def column(self, column_number: int) -> list:
        """
        Returns a list with the column itens for the requested column
        """
        single_column = self.columns()[column_number - 1].split(" ")
        for i in range(len(single_column)):
            single_column[i] = int(single_column[i])
        return single_column


m = Matrix("1 2 3\n4 5 6\n7 8 9")
rows = m.rows()
r = []
for row in m.rows():
    r.append(row.split(" "))
print(len(r[0]))
