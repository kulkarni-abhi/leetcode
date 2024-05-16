"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""

class Solution(object):
  """
  Approach -
  ----------
  1. We use a two-pointer approach,
     starting with left = 0 and the right = height.size() - 1

  2. initialize a variable maxWater = 0

  3. while left pointer is less than the right pointer.

  4. width of container, width = right - left

  5. height of the container, h = min(height[left], height[right])

  6. water capacity of the container, water = width * h

  7. if the current container holds more water than the previous maximum:
     maxWater = max(maxWater, water).

  8. Finally, we adjust the pointers:
     if the height[left] < height[right], move the left pointer to the right (left++);
     otherwise, we move the right pointer to the left (right--).

  9. Repeate steps 4 to 8 until the left pointer >= right pointer

"""
  def maxArea(self, height):
    left = 0      # Left pointer starting from the leftmost edge
    right = len(height) - 1  # Right pointer starting from the rightmost edge
    maxWater = 0    # Initialize the maximum water capacity

    while left < right:
      # Calculate the width of the container
      width = right - left

      # Calculate the height of the container (the minimum height between the two lines)
      h = min(height[left], height[right])

      # Calculate the water capacity of the current container
      water = width * h

      # Update the maximum water capacity if the current container holds more water
      maxWater = max(maxWater, water)

      # Move the pointers towards each other
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1

    return maxWater

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
