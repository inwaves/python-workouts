from sols.ex22 import *


def test_passwd_to_csv() -> None:
    in_filename = "data/pwd"
    out_filename = "data/out"


    # Check file doesn't exist, or is empty first.
    import os
    assert not os.path.exists(out_filename)

    # Run the function.
    passwd_to_csv(in_filename, out_filename)


    lines = ["nobody\t-2", "root\t0", "daemon\t1"]
    # Check that the file contains the rows we expect.
    with open(out_filename) as fileobj:
        it = iter(lines)
        for line in fileobj:
            assert line == next(it)

    # Tear down the file.
    os.remove(out_filename)
