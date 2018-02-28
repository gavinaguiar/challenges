'''
Simple fibonacci sequence
Input: n
Output: fibonacci sequence till n
'''

def fibonacci(n):
	if (n == 0 or n ==1):
		return n
        
        if (memo[n]):
		return memo[n]
	else:
		memo[n] = fibonacci(n-1) + fibonacci(n-2) 
	return memo[n]

n = 10
memo = [None for i in range(n)]
for i in range(n):
	print fibonacci(i)
