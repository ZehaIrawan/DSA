
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



        # res is a variable to store the largest container so far
        # i loop is to iterate heights array from index 0 to the end
        # j loop is to iterate from i+1 until the end of array

        # now for the min max logic
        # min(heights[i], heights[j])
        # The container's height is limited by the shorter line between the two. Water can't be taller than the shortest wall.

        # (j - i):
        # The distance between the two lines — this gives the width of the container.

        # min(...) * (j - i):
        # This gives you the area between lines i and j.

        # max(res, ...):
        #This checks if the current area is larger than the res we’ve saved so far. If it is, it updates res.

        # Logic gist
        # Try every pair of lines. For each pair, calculate the area between them, and keep track of the biggest one.

        # i missed that it's looking for area, i thought it was looking for
        # the amount of water total which is from each height

        # why return 8
        # because the indentation of the return is wrong, should be outside of nested loop

         # Iterate through the array
        # cannot find by just finding 2 biggest number, because there might be smaller number with more value inside

        # i dont think we can use just two pointer technique here
        # sliding window is the best


        # brute force
        # i get the i & j pointer
        # need to understand below
        # max(res, min(heights[i], heights[j]) * (j - i))

        #https://neetcode.io/solutions/container-with-most-water

        # largest_area = 0

        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         largest_area = max(largest_area, min(height[i],height[j]) * (j - i))
        
        # return largest_area

largest_area = 0
# l = 0
# r = len(height)-1
l, r = 0, len(heights) - 1
# can be simplified with one line
# also forgot to -1 from the length because it's 0 based index

while l < r :
# largest_area = max(largest_area, min(height[i],height[j]) * (j - i))
# original statement is too long, better to break it up to 2 variables
    area = min(height[l],height[r]) * (r - l)
    largest_area = max(largest_area, area)
# this is wrong but i can't seem to find the logic for l staying put and test the r
# l += 1
# r += 1
    if height[l] <= height[r]:
# if left side is less or equal to right side height
# move the left side to next side
        l += 1
    else:
# if right  side is smaller the move the right side to the next side    
        r -= 1
return largest_area


# basically this solution starts at first index and last index and then compare the area with one loop