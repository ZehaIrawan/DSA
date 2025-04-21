#Given an array nums, move all the zeroes to the end of it while maintaining the relative order of the non-zero elements.

# Do this in-place with O(1) extra space.
# print(move_zeroes([0, 1, 0, 3, 12]))  => [1, 3, 12, 0, 0]

# keep track the index of first 0
# the basic logic goes if array item value is 0 then do nothing
# if it's not zero swap it with zero

def move_zeroes(nums):
  write_pointer = 0

  for read_pointer in range(len(nums)):
    # if the current array item value is not 0
    if nums[read_pointer] != 0:
      # Swap current element with the element at last_non_zero index
      nums[read_pointer], nums[write_pointer] = nums[write_pointer], nums[read_pointer]
      write_pointer += 1
  return nums

# print(move_zeroes([0, 1, 0, 3, 12]))

# first iteration at index 0, read_pointer = 0
# nums[0] = 0
# do nothing
# write pointer still 0

# 2nd iteration at index 1, read_pointer =1
# nums[1] = 1
# it's not zero so swap the value by using read & write pointer index
# swap nums[0] with nums[1]
# [0, 1, 0, 3, 12] => [1, 0, 0, 3, 12] 
# increase the write pointer
# write pointer = 1

# 3rd iteration at index 2, read_pointer = 2
# nums[2] = 0
# do nothing, nums the same as prev iteration [1, 0, 0, 3, 12]

# 4th iteration at index 3, read_pointer = 3
# nums[3] = 3
# swap the write_pointer which is 1 with current index
# [1, 0, 0, 3, 12] => [1, 3, 0, 0, 12] 
# increase the write pointer to 2

# 5th iteration at index 4, read_pointer = 4
# nums [4] = 12
# swap the write_pointer which is 2 with current index
# [1, 3, 0, 0, 12] => [1, 3, 12, 0, 0] 




# 🔁 Iterations
# read = 0, nums[0] = 0
# → It's zero → do nothing

# read = 1, nums[1] = 1
# → Not zero → swap with write (0)
# → [0, 1, 0, 3, 12] → [1, 0, 0, 3, 12]
# → write += 1 → write = 1

# read = 2, nums[2] = 0
# → It's zero → do nothing

# read = 3, nums[3] = 3
# → Not zero → swap with write (1)
# → [1, 0, 0, 3, 12] → [1, 3, 0, 0, 12]
# → write += 1 → write = 2

# read = 4, nums[4] = 12
# → Not zero → swap with write (2)
# → [1, 3, 0, 0, 12] → [1, 3, 12, 0, 0]
# → write += 1 → write = 3

