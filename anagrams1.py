'''
Given two strings, check if the are anagrams of each other or if they
differ in just one character.
eg Input: toe and tea
Output True


'''

def anagram(str1,str2):
    if(len(str1) != len(str2)):
        return ("Not anagrams. Strings have different lengths")
        
    alphabets = [0 for i in range(26)]
    for i in range(len(str1)):
        alphabets[ord(str1[i]) - 97] +=1
    
    
    for i in range(len(str2)):
        alphabets[ord(str2[i]) - 97] -=1
        
    count =0
    for i in alphabets:
        if i ==1:
            count +=1
    if (count == 0):
        return "%s and %s are anagrams" %(str1,str2) 
    
    print alphabets
    return "%s and %s are not anagrams" %(str1,str2)



str1="qwerty"
str2="ytrewq"
print(anagram(str1,str2))