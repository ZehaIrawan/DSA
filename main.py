# print(move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]

def move_zeroes(nums):
  left = 0

  for right in range(len(nums)):
    # if the value is not 0
    if nums[right] != 0:
      # nums left is 
      print(nums[left], nums[right])

print(move_zeroes([0, 1, 0, 3, 12]))