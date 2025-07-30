class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0

        # use set python
        passed_char = set()

        # sliding window
        for i in range(len(s)):
            while right < len(s):
                # if no duplicate then no need to move left
                # if there is duplicate then increase the left index by 1
                if(s[right] in passed_char):
                    passed_char.remove(s[right])
                    left = right
                else:
                    passed_char.add(s[right])
                    right += 1

        print(left,right)
        print(passed_char)
        return len(passed_char)


        # "abcabcbb"
        # left = a
        #  right = b
        # no duplicate? move the right to next index

        # you need to have both the index and the actual char

# Chatgpt
# You're close, but the current implementation has a few issues that prevent it from correctly finding the length of the longest substring without repeating characters. Let me walk you through the problems and a corrected version.

# ✅ What you're doing right:
# Using a sliding window (left and right) to find substrings.

# Using a set to track characters currently in the window.

# ❌ What's missing / wrong:
# Resetting left = right is incorrect.

# When a duplicate is found, left shouldn't just jump to right, because it might skip over important characters. Instead, you should increment left by one and remove the s[left] character until the duplicate is gone.

# len(passed_char) doesn't always represent the longest substring.

# You need to keep track of the maximum length seen so far.

# The outer loop for i in range(len(s)) is unnecessary.

# Your right pointer already handles the loop, so you only need a while loop.