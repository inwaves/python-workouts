from sols.ex7 import ubbi_dubbi, url_encode

def test_ubbi_dubbi() -> None:
    assert ubbi_dubbi("milk") == "mubilk"
    assert ubbi_dubbi("program") == "prubogrubam"
    assert ubbi_dubbi("octopus") == "uboctubopubus"
    assert ubbi_dubbi("elephant") == "ubelubephubant"


def test_url_encode() -> None:
    assert url_encode("with space") == "with%20space"
