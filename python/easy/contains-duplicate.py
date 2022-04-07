"""
Link: https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

:type nums: List[int]
:rtype: bool
"""

"""
Solution 1: 
time complexity: O(nlogn)
space complexity: O(1)
"""


class Solution1(object):
    def containsDuplicate(self, nums):

        # if the length of the list of numbers is less than 2, return true
        if len(nums) < 2:
            return False
        else:
            # sort the list of numbers
            nums.sort()
            for i in range(len(nums) - 1):
                # if the current index and the next index are the same, a duplicate has been found
                if nums[i] == nums[i + 1]:
                    return True
        return False


test = Solution1()
print(test.containsDuplicate([4, 5, 1, 3, 2]))

"""
Solution 2: 
time complexity: O(n)
space complexity: O(n)
"""


class Solution2(object):
    def containsDuplicate(self, nums):

        # create a has to numbers to
        hashset = set()

        # checks to see if the number in our list exists in the hash set.
        # if it does, then a duplicate has been found
        # if not, then add it to the hash set
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
