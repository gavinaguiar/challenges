'''
Find total number of ways to climb up steps
X is the number of steps allowed to climb at each turn
'''

def num_ways(N,X):
    if N==0:
        return 1
    nums=[0 for _ in range(N+1)]
    nums[0]=1 
    for i in range(1,N+1):
        total=0
        for j in X:
            if i-j >=0:
                total+=nums[i-j]
        nums[i]=total
    return nums[N]


numberOfSteps=6
X=[1,3,5]

print(num_ways(numberOfSteps,X))