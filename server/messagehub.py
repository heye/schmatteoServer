
from typing import Dict
import traceback
from server import file_storage


class cache:
    ret = ""
    names = []

    rage_ret = ""
    rage_names = []
    
    animal_names = []
    animal_names_ret = ""
    
    nuzzle_ret = ""
    nuzzle_names = []


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
        if len(cache.names) > 80:
            cache.names.pop(0)
            
            fist_line_length = 0
            for c in cache.ret:
                fist_line_length  = fist_line_length + 1
                if c == '\n':
                    break
            cache.ret = cache.ret[fist_line_length:]
            print("FIRST LINE LEN " + str(fist_line_length))

        file_storage.write_file(cache.ret)
        return "added"

    else:
        print(cache.names)
        cache.names.remove(name)
        cache.names.append(name)
        print(cache.names)

        #double buffer, so the returned list is always full
        new_ret = ""
        for one_name in cache.names:
            new_ret += one_name + "\n"
            cache.ret = new_ret

    return "already_exists"


def handleAddRage(name: str) -> str:

    if name not in cache.rage_names:
        cache.rage_names.append(name)        
        cache.rage_ret += name + '\n'
        return "added"

    return "already_exists"


def handleGetRage() -> str:
    temp = cache.rage_ret
    cache.rage_ret = ""
    cache.rage_names = []
    return temp


def handleAddNuzzle(name: str) -> str:

    if name not in cache.nuzzle_names:
        cache.nuzzle_names.append(name)        
        cache.nuzzle_ret += name + '\n'
        return "added"

    return "already_exists"


def handleGetNuzzle() -> str:
    temp = cache.nuzzle_ret
    cache.nuzzle_ret = ""
    cache.nuzzle_names = []
    return temp


def handleSetAnimals(animals: str) -> str:
    #print(animals)
    for one_name in animals.splitlines():
        if one_name not in cache.animal_names:
            cache.animal_names.append(one_name)
    
    print("ANIMALS")
    print(cache.animal_names)

    return "set"


def handleGetAnimals() -> str:
    cache.animal_names_ret = ""
    for one_name in cache.animal_names:
        cache.animal_names_ret += one_name + "\n"

    return cache.animal_names_ret


def handleClear() -> str:
    cache.ret = ""
    cache.names = []
    cache.rage_ret = ""
    cache.rage_names = []
    file_storage.write_file("")
    return "cleared"