def floorOfSqrt(num):
    if (num == 0 or num == 1) : 
        return num 

    start=1
    end=num
    ret=0
    while(start<=end):
        mid=(start+end)//2
        square=mid*mid
        if square == num:
            return mid
        else:
            if square>num:
                end=mid-1
            else:
                start=mid+1
                ret=mid
    return ret  


                

num=9
print(floorOfSqrt(num))