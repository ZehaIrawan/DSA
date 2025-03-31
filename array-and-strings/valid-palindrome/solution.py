class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non-alphanumerice characters
        # convert to lowercase
        # split string to characters in an array
        # reverse the string, then split to array
        # iterate through both array, compare

        # for python we can use isalnum() for a string to check if it's alpha numeric
        # we can use for loop for each char in a string
        chars = []

        for char in s:
            if char.isalnum():
                chars.append(char.lower())

        reversed_chars = chars[::-1]

        if chars == reversed_chars:
            return True
        return False
        
        # Issues
        # You're seeing u before each character because you're likely using Python 2, where Unicode strings are prefixed with u.
        # The issue is that .reverse() modifies the list in place and returns None instead of returning a new reversed list.
        # to reverse array in python is slicing [::-1] or list(reversed(arr))
        # no need to iterate array, just compare it

# Combined to 2 lines of code
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         check = "".join([char.lower() for char in s if char.isalnum()])
    
#         return check == check[::-1]