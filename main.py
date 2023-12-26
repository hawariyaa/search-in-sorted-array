# the problem is searching for a number in a sorted array, when found return the index
# if the number doesn't exist then return the index where it would be if it was in the array
# so the time complexity should be O(log n) not O(n)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg = 0
        end = len(nums) - 1
        while beg <= end:
          cur = (beg + end) // 2 # integer division needs // example 5 // 2 = 2
          if target == nums[cur]:
            return cur
          elif target < nums[cur]:
            end = cur - 1
          elif target > nums[cur]:
            beg = cur + 1
        return beg
