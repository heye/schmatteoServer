
from typing import Dict
import traceback
from server import file_storage


class cache:
    ret = ""
    names = []

def setup():
    file_storage.setup()
    cache.ret = file_storage.read_file()

    for one_name in cache.ret.splitlines():
        if one_name not in cache.names:
            cache.names.append(one_name)
    
    print("INIT")
    print("READ " + cache.ret)
    print("PARSED " + str(cache.names))


def handleGet() -> str:
    return cache.ret

def handleAdd(name: str) -> str:

    if name not in cache.names:
        cache.names.append(name)        
        cache.ret += name + '\n'
        file_storage.append_file(name + '\n')
        return "added"
    

    return "already_exists"

def handleClear() -> str:
    cache.ret = ""
    cache.names = []
    file_storage.write_file("")
    return "cleared"