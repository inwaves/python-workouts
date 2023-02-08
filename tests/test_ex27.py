from sols.ex27 import *

def test_create_pwd_generator() -> None:
    assert True


def test_create_pwd_checker() -> None:
    fn = create_pwd_checker(2, 5, 1, 1)
    assert fn("BooHoo13!") == False
    assert fn("BoooHoo13!") == True
