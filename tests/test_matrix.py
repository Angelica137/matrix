from scripts.matrix import *


def test_matris_returns_input_string():
    m = Matrix("1 2 3\n4 5 6\n7 8 9")
    assert m.numbers == "1 2 3\n4 5 6\n7 8 9"
