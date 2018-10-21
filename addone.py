def addone(myarr):
    carry=1
    for i in range(len(myarr)-1,-1,-1):
        sum=myarr[i]+carry
        if sum >= 10:
            carry=1
        else:   
            carry=0
        myarr[i]=sum%10

    if carry == 1:
        return [1] + myarr
    return myarr
    


myarr=[9,9,9]
print addone(myarr)