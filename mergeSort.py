def mergeSort(myarr):
    if len(myarr) <= 1:
        return myarr

    mid=(len(myarr))/2
    lefthalf=mergeSort(myarr[:mid])
    righthalf=mergeSort(myarr[mid:])
    return merge(lefthalf,righthalf)
    

def merge(lefthalf,righthalf):
    ret=[]
    
    while(len(lefthalf)!=0 and len(righthalf)!=0):
        if lefthalf[0]<righthalf[0]:
            ret.append(lefthalf[0])
            lefthalf.remove(lefthalf[0])
        else:
            ret.append(righthalf[0])
            righthalf.remove(righthalf[0])

    if len(lefthalf) == 0:
        ret += righthalf
    else:
        ret += lefthalf

    return ret             


   

myarr=[453,56856,23432,58,2569,4,8906]
print(mergeSort(myarr))