# Name: Russ Arnold 
# Evergreen Login: arnrus09     
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2



###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

# The following function, "Gauss", takes a positive integer and adds it will all 
# positive integers of lesser value.  It returns the result.

def Gauss(n):
    t = 0
    if n > 0 and type(n) == int:
        while n > 0:
            t = t+n
            n = n-1
        print t
    else: print "This function only accepts positive intiger arguments"

from hw2_test import n

Gauss(n)


###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

# Function, "res" divides 1 by a positive intiger,n and seperately divides 1 by each 
# positve integer of a lesser value than n.  The product of each operation is printed.

def res(n):
    for i in range(1,(n+1)):
       print 1.0/i
n = 10

res(n)

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

# "TriangleNum" is a function that gives the triangle number of positive integers

n = 10
def TriangleNum(n):
    triangular = 0
    if n > 0:
        for i in range(n+1):
                triangular += i
        print "Triangular number", n, "via loop:", triangular
        print "Triangular number", n, "via formula:", n*(n+1)/2
    else: print "ERROR!!!: No negatives"   

TriangleNum(n)

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

# "fac", a function, gives the factorial of any positive whole number.

n = 10

def fac(n):
    ans = 1
    if n > 0:
        for i in range(n):
               ans *= (i+1)
        print ans
    else: print "ERROR!!!: No negatives"   
    
fac(n)

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

# This function is called "multifac".  It gives the factorial of a positive integer, n
# and the factorials of all positive integers of lesser value.

numlines = 10

def multifac(n):
    ans = 1
    if n > 0:
        for i in range(n, 0, -1):
           ans = 1
           for j in range(i):
              ans = ans*(j+1)
           print ans
    else: print "ERROR!!!: No negatives"   
multifac(numlines)
      

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

# The following, a function called "sumfacres", adds 1 divided by a natural number, n with 
# one divieded by each of the natural numbers of lesser value.

def sumfacres(n):
    z = 1.0
    x = 1.0
    y = 1.0
    if n > 0:
       for i in range(n):
          x *= (i+1)
          z = 1/x
          y += z
       print y
    else: print "ERROR!!!: No negatives"   

sumfacres(numlines)
###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
