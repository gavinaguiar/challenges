#!/usr/bin/env python3
from collections import Counter

def isPrime(n):
    '''
    List comprehension  
    filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 13))
    '''
    if n <=1:
        return False
    
    for i in range(2,n):
        if (n%i == 0):
            return False
    return True

words = ["blah" , "car" , "tree", "boy", "girl", "arc" , "oby" , "rac"]
alphabetList = []
n,i=0,0
while i<26:
    if isPrime(n):
        alphabetList.append(n)
        i+=1
    n+=1

values = []
for word in words:
    value = 1
    for w in word:
        value *= alphabetList[ord(w)-97]
    values.append(value)
    
myDict = Counter(values)
for key,val in myDict.items():
    if val > 1:
        indices = [i for i, x in enumerate(values) if x == key]
        print(' '.join([words[item] for item in indices]), " are anagrams")
               
               
               