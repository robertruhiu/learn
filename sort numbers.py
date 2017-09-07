def large_small(*args):
    large=small=args[0]
    for arg in args:
        if arg>large:
            large=arg
        if arg<small:
            small=arg
    print(small)
    print(large)
large_small(1,3,-2,9,5)
