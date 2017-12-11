#!/usr/bin/python
 
sol = sum(([x for x in range(1,1000) if (x%3)==0 or x%5==0]))

print "Sum of all the multiples of 3 and 5 below 1000 is %s" %(sol) 

