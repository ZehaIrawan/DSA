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



# two pointer (indices)
# use a while loop, as long as first pointer (left) is less than the second pointer (left)
# left pointer at the start of the array
# right poitner at the end of the array
# after each iteration:
#   move the left pointer to right by 1
#   move the right pointer to left by 1


def isPalindrome(word):
  l = 0
  r = len(word) - 1

  while l < r:
    # you have acess to the first char and last char on every loop
    if(word[l] != word[r]):
      return f"{word} IS NOT A PALINDROME!"

    l += 1
    r -= 1
  return f"{word} IS A PALINDROME!"

print(isPalindrome('MADAM'))
print(isPalindrome('NURSE'))
print(isPalindrome('ROTOR'))
print(isPalindrome('RACECAR'))
print(isPalindrome('TOYOTA'))