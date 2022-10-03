"""File contains util methods used by all modules"""

def size(byte) -> str:
    for x in ["B","KB","MB","GB","TB"]:
        if byte < 1024:
            return f"{byte:.2f} {x}"
        byte=byte/1024
