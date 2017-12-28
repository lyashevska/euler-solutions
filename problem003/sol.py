def factor(x):
    factors = []
    i = 2
    while x > 1:
        if x % i == 0:
            x = x // i
            factors.append(i)
        else:
            i+=1
    return factors

n = 600851475143
print ('The maximum prime factor of the number %s is %s' % (n, max(factor(n))))
