def unique_extensions() -> set:
    import os
    ext = lambda filename: f".{filename.split('.')[-1]}" if '.' in filename else ''
    res = set(ext(s) for s in os.listdir("sols/"))
    res.remove('')
    return res
