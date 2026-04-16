# indices = plural of 'index'

# since we are looking for 2 combination of numbers
# the naive approach is a brute force
# we use nested loops to check if the number adds up to a target


# for loop will return the number but not the index
# so we will need to use range
# for x in range(6):
# https://www.w3schools.com/python/python_for_loops.asp

# Mistake 1
# Trying to iterate more than nums length

# for i in range(len(nums)):
#   for j in range(len(nums)+1):
#     print(nums[i],nums[j])
# IndexError: list index out of range

# Solution: range can accept 2 params instead of 1 and start at specific index

# Mistake 2
# invalid syntax
# f nums[i] + nums[j] == target
# forgot :

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

# Runtime 2046ms
# Memory 13.3MB