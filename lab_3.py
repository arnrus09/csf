series = 'sum'
n = 7



def fib(n):
	if n==1 or n==0:
		return 1
	return fib(n-1) + fib(n-2)



def lab_3():
        if series == 'fibonacci':
                print fib(n)
        elif series == 'sum':
                print (sum(range(0,3*n+1,3)))

        else:
                print 'null'

lab_3()          
              

series = 'fibonacci'
n = 17

lab_3()



series = 'nothing'


lab_3()
t = 0

