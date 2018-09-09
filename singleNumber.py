'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
'''



def singleNumber(nums):
     xor=nums[0]
     
     for n in range(1,len(nums)):
         xor = xor^nums[n]
    
     bit = xor ^ ~(xor-1)
     num1=0
     num2=0
     
     for num in nums:
        if(num & bit) > 0:
            num1 = num1^num
        else:
            num2 = num2^num
     
     
     return num1 , num2

nums = [1, 2, 1, 3, 2, 5]
print(singleNumber(nums))