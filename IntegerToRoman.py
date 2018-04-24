from test.support import temp_cwd
symbols = {1 : "I", 
           5 : "V",
           10 : "X",
           50 : "L",
           100 : "C",
           500 : "D",
           1000 : "M"}


def intToRoman(num, ret = ""):
    strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]        
    ret = ""        
    for i, j in enumerate(nums):
        while num >= j:
            ret += strs[i]
            num -= j
            if num == 0:
                return ret

print(intToRoman(9))