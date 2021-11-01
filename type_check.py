def only_ints(a, b):
    if (type(a) is int and type(b) is int):
        return True
    else: return False

print(only_ints(1, 2))

print(only_ints(1.0, 2))

