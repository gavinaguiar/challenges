'''
 find the length of the longest substring without repeating characters.
'''

def distinctSubstring(s):
    if len(s) <= 0:
        return len(s)
    ret=[]
    maxlength=0
    for c in s:
        if c in ret:
            ret=ret[ret.index(c)+1:]
            ret.append(c)
        else:    
            ret.append(c)

        maxlength=max(maxlength,len(ret))
    return max(maxlength,len(ret))

s="dvdf"
print(distinctSubstring(s))