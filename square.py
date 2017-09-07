def square_me(*args):
    square = []
    for i in args:
        square.append(i**2)
    return (square)

print(square_me(1,9,36,4))
