"""
Link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        thisdict = {}
        # iterate through each item
        for index in range(len(nums)):
            # this is the value we are going to be searchign for in our lists to see if we have a match
            difference = target - nums[index]
            # if the difference is in our hash, we have found our match. Append to output array and done.
            if difference in thisdict:
                output.append(index)
                output.append(thisdict[target - nums[index]])
                break
            # if not, then add current value and index to our hash map and continue the serach
            else:
                thisdict[nums[index]] = index

        return output


test = Solution()
print(test.twoSum([1, 2, 3, 4, 5, 6, 7, 8], 11))


""" 
----- ANALYSIS -----
This can be done in O(n^2) by using nested loops - first loop to iterate through the list entirely, and the second loop
to start wherever the index is currently at, searching for a possible match

However, this can be improved upon via hashing. if you hash ever value youve previously encountered, then you can use the 
difference needed from the current value and the target as the hash key and find out in constant time if you have a pairing
"""
