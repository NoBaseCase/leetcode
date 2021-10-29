'''
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        # iterate every item except for the last one in the list
        for position in range(0, len(nums)-1):
            # iterate through every item starting at index position
            for current in range(position+1, len(nums)):
                # if the two indexes match the target, add them to output list and return
                if(nums[position] + nums[current] == target):
                    output.append(position)
                    output.append(current)
                    return output
        return output

test = Solution()
print(test.twoSum([1,2,3,4,5,6,7,8], 11))