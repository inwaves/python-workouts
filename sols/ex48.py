from typing import Generator
import os


def file_gen(dirname: str) -> Generator:
    for dirname, _, files in os.walk(dirname):
        for file in files:
            with open(os.path.join(dirname, file)) as fileobj:
                for line in fileobj:
                    yield line
