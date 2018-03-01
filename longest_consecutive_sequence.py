'''
Longest consecutive sequence in an array

Input: [2,1,6,9,4,3]
Output: 4 -> 1,2,3,4
'''

def lcs(inputList):
    maxSum = 0
    currSum = 0
    myDict = {i : True for i in inputList}
    for n in myDict:
         if (n-1 in myDict):
            continue
         currSum+=1
         curr = n
         while(True):
            if (curr+1 in myDict):
                currSum+=1
                curr+=1
            else:
                break
         if (currSum > maxSum):
             maxSum = currSum
         currSum=0
         return maxSum

inputList = [2,1,6,9,4,6,3,5]
print lcs(inputList)

    