"""
link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

:type nums: List[int]
:type target: int
:rtype: List[int]
"""


class Solution(object):
    def twoSum(self, nums, target):
        # create a has map that stores the value and keys of items in the list
        hashmap = {}

        # iterate through the number list
        for n in range(len(nums)):
            difference = target - nums[n]
            # check to see if the difference of the current number and the target are a key in the hashmap
            if difference in hashmap:
                # if it is, return the current index and the value of the differences location in the hashmap
                return [n, hashmap[difference]]
            else:
                # add current value to hashmap
                hashmap[nums[n]] = n
        return []


test = Solution()
print(test.twoSum([3, 3], 6))
