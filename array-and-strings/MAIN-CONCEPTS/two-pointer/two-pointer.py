# The two-pointer technique is one of the most powerful tools in your problem-solving toolbox, especially for array and string problems.

#🧠 What is the Two Pointer Technique?
#You use two variables (pointers) to iterate over a list — either from the start and end, or both from the start — to efficiently find answers without checking every possible combination.

#It helps reduce O(n²) brute force to O(n) or O(n log n).

numbers = [1, 2, 3, 4, 6]

target = 7

#for i in range(len(numbers)):
#  print(numbers[i])


# define first pointer (left)
# define second pointer (right)
# in this sorted array case we define it as index 0 and last index
# use while loop and then move the pointers


# def has_pair_with_sum(numbers,target):
#   left = 0
#   right = len(numbers) - 1

#   while left < right:
#     current_sum = numbers[left] + numbers[right]
#     if current_sum == target:
#       return True
#     elif current_sum < target:
#       left += 1
#     else:
#       right -= 1

#   return False

# print(has_pair_with_sum(numbers,target))



# can be used on

# 1. ✅ Check if Array has a Pair that Sums to Target (Two Sum) 
#     https://leetcode.com/problems/two-sum

# 2. ✅ Reverse a String / Array In-Place
#     https://leetcode.com/problems/reverse-string/description/

# 3. ✅ Remove Duplicates in a Sorted Array
#     https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# 4. ✅ Move Zeroes to End
# 5. ✅ Palindrome Check

