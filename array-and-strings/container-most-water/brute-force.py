
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49


def maxArea(heights):
  res = 0
  for i in range(len(heights)):
    for j in range(i + 1, len(heights)):
      res = max(res, min(heights[i], heights[j]) * (j - i))
    return res

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