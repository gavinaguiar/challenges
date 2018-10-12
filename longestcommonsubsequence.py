
def LCS(str1,str2,m,n):
    if memo[m][n]:
        return memo[m][n]
    if  m ==0 or n ==0:
        return 0
    if str1[m-1] == str2[n-1]:
        result = 1+LCS(str1,str2,m-1,n-1)
    elif str1[m-1] != str2[n-1] : 
        result= max(LCS(str1,str2,m-1,n),LCS(str1,str2,m,n-1))
    memo[m][n] = result
    return result


m="AGGTAB"
n="GXTXAYB"
memo=[[0 for i in range(len(n)+1)] for j in range(len(m)+1)]
print LCS(m,n,len(m),len(n))