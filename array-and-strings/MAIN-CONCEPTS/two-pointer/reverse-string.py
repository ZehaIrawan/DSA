# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.



# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Use two pointer, one at the start
        # and one at the end

        read = len(s) - 1
        # print(len(s) % 2 == 0)
        for write in range(len(s)):
            # s[write] = s[read]
            # s[read] = s[write]

# Mistake 1
# Instead of assigning one by one like above we can use
# s[write], s[read] = s[read], s[write]

# Mistake 2
# need >= instead of just >


        # if the read pointer(last) is not in the center of string
        # checking via dividing array length by half

        # need to check even or odd for the array length
            if(read >= len(s) / 2):
                s[write], s[read] = s[read], s[write]
                read -= 1

# 🔍 Your Logic Summary
# You're:
# 1. Using two pointers: write from start, read from end.
# 2. Swapping characters until the two meet in the middle.
# 3. Trying to avoid unnecessary swaps after the midpoint.

# This is correct in spirit, but there are a few issues we can clean up.

# ⚠️ Issues in Your Code
# ❌ 1. You're swapping write and read on every write loop iteration, even beyond the midpoint, which is unnecessary.
# for write in range(len(s)):
#     if(read >= len(s) / 2):  # trying to stop halfway
#         s[write], s[read] = s[read], s[write]
#         read -= 1
# ✅ Better: stop when write >= read — no need to compare with len(s)/2.

# ❌ 2. This condition:
# if read >= len(s) / 2
# Is a bit overcomplicated. Instead, just loop while write < read.

# ✅ Improved Version (Clean + Idiomatic)
# def reverseString(self, s: List[str]) -> None:
#     left, right = 0, len(s) - 1

#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1

# You're swapping the first element with the last, the second with the second-last, and so on — stopping when the pointers meet or cross.

# Length Type	    Does it affect logic?	  Action Needed
# Even	          No	                    Just swap normally
# Odd	            No	                    Middle element stays untouched
