from sols.ex3 import *

def test_run_timing() -> None:
    # assert run_timing() == (15.0, 3)
    pass


def test_crop_float() -> None:
    assert crop_float(1234.5678, 2, 2) == 34.56
