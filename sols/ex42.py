from typing import Any


class FlexibleDict(dict):
    def __getitem__(self, key: str | int) -> Any:
        if key in self:
            return dict.__getitem__(self, key)
        else:
            if isinstance(key, str):
                try:
                    key_asint = int(key)
                    if key_asint in self:
                        return dict.__getitem__(self, key_asint)
                except ValueError:
                    raise KeyError("Key not present in dictionary!")
            elif isinstance(key, int):
                key_asstr = str(key)
                if key_asstr in self:
                    return dict.__getitem__(self, key_asstr)
                else:
                    raise KeyError("Key not present in dictionary!")
