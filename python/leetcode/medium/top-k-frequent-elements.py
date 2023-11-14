"""
link: https://leetcode.com/problems/top-k-frequent-elements/
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):  # has map to store number frequency data
        count = {}
        # initializes an array of n lists, where n is the length of nums
        frequency = [[] for i in range(len(nums) + 1)]

        # add the frequency of each number to a hash
        for n in nums:
            # if n is not within count, it will add it to the dictionary
            count[n] = 1 + count.get(n, 0)

        # the count of a number will act as the index of its value in the frequency array
        for n, c in count.items():
            frequency[c].append(n)

        output = []

        # once the 2D frequency list has been generated,
        # traverse from the end to the beginning, appending the first k elements to the output list
        # once the length of the output list is equal to k, return the output list
        for index in range(len(frequency) - 1, 0, -1):
            for value in frequency[index]:
                output.append(value)
                if len(output) == k:
                    return output


test = Solution()
print(test.topKFrequent([3, 2, 2, 1, 1, 1], 3))
