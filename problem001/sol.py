#!/usr/bin/python
 
mmax = 1000
m3 = sum(range(3, mmax, 3))
m5 = sum(range(5, mmax, 5))
m15 = sum(range(15, mmax, 15))

print "Sum of all the multiples of 3 and 5 below 1000 is %s" %(m3+m5-m15) 

