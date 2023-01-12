from sols.ex4 import *

def test_hex_output() -> None:
    assert hex_output(5) == 5
    assert hex_output("AF") == 175
    assert hex_output("0") == 0
    assert hex_output("0x1f") == 31
