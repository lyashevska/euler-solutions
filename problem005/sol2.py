#!/usr/bin/python

def gcd(x,y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x,y):
    return x*y // gcd(x,y)

def lcm_list(x,*args):
    for y in args:
        x = lcm(x,y)
    return x

answer = lcm_list(*range(1,21))


