#!/usr/bin/python

from common import primeSieve
from math import sqrt, log

def lcm(N):
    primes=primeSieve(N+1) 
    sqrtN=sqrt(N)
    ans=1
    for p in primes:
        if p <= sqrtN:
            ans*=p**(int(log(N)/log(p)))
        else:
            ans*=p
    return ans

print lcm(20)
