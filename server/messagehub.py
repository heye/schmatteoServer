
from typing import Dict
import traceback

names = []

def handleGet() -> str:
    ret = ""
    for one_name in names:
        ret += one_name + '\n'
    return ret

def handleAdd(name: str) -> str:

    if name not in names:
        names.append(name)
        return "added"

    return "already_exists"

def handleClear() -> str:
    names = []
    return "cleared"