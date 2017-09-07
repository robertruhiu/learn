def add_all(*args):
    total = 0
    for i in args:
        total=i+total
    return (total)

print(add_all(2,3,6,8,2))
