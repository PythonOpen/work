def add(data):
    sum = 0
    for i in data:
        sum = sum + i
    return sum


def add(*data):
    sum = 0
    for i in data:
        sum = sum + i
    return sum


def add(**data):
    print(data)



