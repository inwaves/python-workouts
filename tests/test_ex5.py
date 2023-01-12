from sols.ex5 import *

def test_pig_latin() -> None:
    assert pig_latin("Python") == "Ythonpay"
    assert pig_latin("air!") == "airway!"
    assert pig_latin("eat") == "eatway"
    assert pig_latin("Computer,") == "Computerway,"
