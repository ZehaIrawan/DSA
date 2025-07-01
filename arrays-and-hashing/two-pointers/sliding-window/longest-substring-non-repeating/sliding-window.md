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
def lengthOfLongestSubstring(s):
    char_set = set()                 
    # Set to store characters in the current window

    # In Python, a set is a built-in data type that represents an unordered collection of unique elements. It is one of Python's four fundamental collection types, alongside lists, tuples, and dictionaries, each serving different purposes. 

    left = 0                         
    # Left pointer for the sliding window

    max_length = 0                  
    # Variable to track the maximum length found

    for right in range(len(s)):     
        # Move the right pointer from 0 to end of string

        while s[right] in char_set: 
            # If the current character is already in the set (duplicate)...

            char_set.remove(s[left]) 
            # Remove the leftmost character from the set

            left += 1               
            # Shrink the window by moving the left pointer to the right

        char_set.add(s[right])      
        # Add the current character to the set (now it's unique in the window)

        max_length = max(max_length, right - left + 1) 
        # Update max length if current window is longer

    return max_length               
    # Return the length of the longest substring without repeating characters

```

Let’s use: s = "abcabcbb"
| Step | `left` | `right` | char | Set       | Max Length |
| ---- | ------ | ------- | ---- | --------- | ---------- |
| 1    | 0      | 0       | a    | {a}       | 1          |
| 2    | 0      | 1       | b    | {a, b}    | 2          |
| 3    | 0      | 2       | c    | {a, b, c} | 3          |
| 4    | 0→1    | 3       | a    | {b, c, a} | 3          |
| 5    | 1→2    | 4       | b    | {c, a, b} | 3          |
| 6    | 2→3    | 5       | c    | {a, b, c} | 3          |
| 7    | 3→4    | 6       | b    | {a, c, b} | 3          |
| 8    | 4→5    | 7       | b    | {a, c, b} | 3          |
