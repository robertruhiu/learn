def get_primes(start,end):

    for var in range(start,end+1):
        is_prime=True
        for divide in range(2,var):
            if var%divide==0:
                is_prime=False
        if is_prime:
            return (get_primes)
print (get_primes)
get_primes(2010,3051)
