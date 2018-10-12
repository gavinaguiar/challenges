
def knapSack(W,n):
    if memo[W][n]:
        return memo[W][n]
    if (n==0 or W==0) :
        return 0
    elif (wt[n]>W):
        return knapSack(W,n-1)
    else:
        temp1=knapSack(W,n-1)
        temp2=val[n] +knapSack(W,n-1)
        result = max(temp1,temp2)
    memo[W][n] = result
    return result


val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50 
memo = [[0 for i in range(len(val)+1)]  for i in range(W+1)] 
print knapSack(W ,len(val)-1)
