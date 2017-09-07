def is_even(n):
    return (n%2==0)
def is_divisible_by_3(n):
    return (n%3==0)
for x in range(15,69):
    if is_even(x) and is_divisible_by_3(x):
        print("{} is even and divisible by 3".format(x))
