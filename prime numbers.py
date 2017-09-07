def get_primes(*args):
    pass
    for var in range(50,201):
        is_prime=True
    for divide in range(2,var):
        if (var%divide==0):
            is_prime=False
    if(is_prime):
        return (var)
get_primes(105,200)
