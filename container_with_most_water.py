'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
'''
class Solution:
    def max_area(height):
        left_line = 0
        right_line = len(height) - 1
        max_area = 0
        
        while left_line < right_line:
              #Next let's calculate the area with the current lines
              starting_area = min(height[left_line], height[right_line]) * (right_line - left_line)
              # Update the maximum area that has been found so far.
              max_area = max(max_area, starting_area)
              
              # Next let's move our pointer and point to the shorter line inward
              if height[left_line] < height[right_line]:
                  left_line += 1
              else:
                  right_line -= 1
        return max_area
    
height = [1,8,6,2,5,4,8,3,7]