
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# Finding maximum amount of water, which is an area of a square, height * width
# the largest answer is 8 on index 1 and 7 on the last index
# since slanted container will spill water, then the highest is 7 x 7 = 49
# 7 is not from the side, it's from the width

def maxArea(heights):
  res = 0
  for i in range(len(heights)):
    for j in range(i + 1, len(heights)):
      # max( => to find max area
      # min(left side height, right side height) to find the lowest side height
      # right side position - left side position is to find the width
      # max(largest_area, min(left side, right side) * (right side position - left side position))
      res = max(res, min(heights[i], heights[j]) * (j - i))
  return res

# iteration 1
# max(0, min(1, 8) * (1 - 0) )
# max(0, 1 * 1)
# res = 1



print(maxArea([1,8,6,2,5,4,8,3,7]))

