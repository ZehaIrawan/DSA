🎯 Idea
We use a sliding window approach:

Start with an empty window and expand it by moving the right pointer.

If a duplicate character is found, shrink the window from the left side until the duplicate is gone.

🧠 Logic
Initialize a set to store characters currently in the window.

Use two pointers: left and right.

Move right forward one character at a time.

If s[right] is not in the set, add it and update the max length.

If s[right] is already in the set, it means there's a duplicate:

Remove characters from the left side of the window until the duplicate is removed.

Keep updating the max length as you go.

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left +1)
        return max_length
```