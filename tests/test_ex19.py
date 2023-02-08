from sols.ex19 import *

def test_passwd_to_dict() -> None:
    assert passwd_to_dict("data/passwd") == {"nobody": -2, "root": 0, "daemon": 1}
