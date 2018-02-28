'''
Simple fibonacci sequence
Input: n
Output: fibonacci sequence till n
'''

def fibonacci(n):
	if (n == 0 or n ==1):
		return n

	return fibonacci(n-1) + fibonacci(n-2)

start = 0
end = 10

for i in range(start,end):
	print fibonacci(i)
