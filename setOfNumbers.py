def countSet(n,k):
    memo={}
    return rec(n,k,len(n)-1,memo)    

def rec(nums,total,i,memo):
    key = str(total) + ":" + str(i)
    if key in memo:
        return memo[key]
    if total==0:
        return 1
    elif i<0:
        return 0
    elif total < 0:
        return 0
    elif total < nums[i]:
        result =  rec(nums,total,i-1,memo)

    result = rec(nums,total,i-1,memo) + rec(nums,total-nums[i],i-1,memo)
    memo[key] = result
    return result


nums=[2,4,6,10]
total=16
print(countSet(nums,total))