def is_file(name):
    from pathlib import Path
    file = Path(name)
    if file.is_file() is True:
        return True
    return False


def is_dir(name):
    from pathlib import Path
    dr = Path(name)
    if dr.is_dir() is True:
        return True
    return False


def readf(name):
    f = open(name, "r")
    return f.read()


def current_path():
    import pathlib
    return str(pathlib.Path().absolute())
