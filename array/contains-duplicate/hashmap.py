# Mistake 1
# In python boolean is capitalized: False not false like in JS

# Mistake 2
# If i assign dictionary after if check, test case 1 & 3 fail
# for num in range(len(nums)):
#     if num in occurances:
#         return True
#     occurances[num] = 1

# If i assign before if check
# for num in range(len(nums)):
#     occurances[num] = 1
#     if num in occurances:
#         return True
# Test case 2 failing, which is [1,2,3,4]
# because the number already exist in dictionary at first run

# Mistake 3
# After console logging the dictionary,
# I realized I made the mistake of using
# for num in range(len(nums)) which will save the index as key
# Instead of for num in nums which will use the number as key

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

    # declare dictionary to keep count
    # loop through nums and save the number as key and occurances as values
    # if at any time key already exist in dictionary return true
    # else return false
        occurances = {}

        for num in nums:
            if num in occurances:
                return True
            occurances[num] = 1
        return False

# time complexity of O(n)
# space complexity of O(n)
# Runtime 12ms
# Memory 24MB


# Optimized solution with set

# return len(nums) != len(set(nums))

# ✅ Use a set instead of a dict because:
# ✔ Less memory overhead (no need for key-value pairs)
# ✔ Faster lookups (optimized for membership checks)
# ✔ More concise code