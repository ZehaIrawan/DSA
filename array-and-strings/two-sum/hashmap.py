# Instead of nested loops, we can use one loop
# And lookup the target in a dictionary where it's faster

# Declare a dictionary
# Calculate the complement value via substracting target with current number in the loops

# Problem 1

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """

#         indices = {}

#         for i in range(len(nums)):
#             complement = target - nums[i]
#             indices[complement] = i
#             if complement in indices:
#                 return [nums[i], indices[complement]]
#         return []

# Your twoSum implementation has a logic issue that prevents it from working correctly. Here’s what’s wrong:

# Issues in Your Code:
# Incorrect Order of Operations:

# You store the complement in the dictionary before checking if it's already there.
# This means that the check if complement in indices: always fails for the first occurrence of a number.
# Returning Incorrect Values:

# You need to return indices, not the values themselves.
# Your return statement is return [nums[i], indices[complement]], but it should be return [indices[complement], i].

# Instead of using range, we can use enumerate
# https://www.w3schools.com/python/ref_func_enumerate.asp

# Save indices[num] = i instead of indices[complement] = i
# Because you want all number to indices

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        indices = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in indices:
                return [i, indices[complement]]
            indices[num] = i
        return []    

# Runtime 0ms
# Memory 12.9MB