from scripts.matrix import *


def test_matris_returns_input_string():
    m = Matrix("1 2 3\n4 5 6\n7 8 9")
    assert m.numbers == "1 2 3\n4 5 6\n7 8 9"


def test_matrix_returns_rows():
    m = Matrix("1 2 3\n4 5 6\n7 8 9")
    assert m.rows() == ["1 2 3", "4 5 6", "7 8 9"]
