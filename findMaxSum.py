'''
Given a list, return the sum of the 2 largest numbers
'''

arr=[15, 9, 7, 11 , 2 , 20]

def findMaxSum(arr):
    max1=arr[0]
    max2=0
    for n in arr:
        if max2 < n:
            if max1 < n:
                max2=max1
                max1=n
            else:
                max2=n
    return max1+max2


print findMaxSum(arr)