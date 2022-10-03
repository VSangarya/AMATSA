"""File contains util methods used by all modules"""

def size_in_gb(byte) -> int:
    return round(byte/1024**3, 2)
