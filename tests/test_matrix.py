from scripts.matrix import *


def test_matris_returns_input_string():
    m = Matrix("1 2 3\n4 5 6\n7 8 9")
    assert m.matrix_string == "1 2 3\n4 5 6\n7 8 9"


def test_matrix_returns_rows():
    m = Matrix("1 2 3\n4 5 6\n7 8 9")
    assert m.rows() == [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def test_row_returns_single_row_1():
    m = Matrix("1")
    assert m.row(1) == [1]


def test_row_returns_single_row_1():
    m = Matrix("1 2 3\n4 5 6\n7 8 9")
    assert m.row(1) == [1, 2, 3]


def test_matrix_returns_columns():
    m = Matrix("1 2 3\n4 5 6\n7 8 9")
    assert m.column(1) == [1, 4, 7]


def test_columns_returns_columns_2():
    m = Matrix("89 1903 3\n18 3 1\n9 4 800")
    assert m.column(1) == [89, 18, 9]


def test_column_returns_single_column_1():
    m = Matrix("1")
    assert m.column(1) == [1]


def test_column_returns_column_2():
    m = Matrix("89 1903 3\n18 3 1\n9 4 800")
    assert m.column(2) == [1903, 3, 4]
