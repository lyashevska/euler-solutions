i, j = 1, 1
MAXIMUM = 4000000
tot = 0

while i <= MAXIMUM:
    if i % 2 == 0:
        tot += i
    i, j = j, i+j 
print ("The sum of the even-valued elements is %s" % (tot))

