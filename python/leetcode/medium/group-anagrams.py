'''
link: https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 
'''


"""
:type strs: List[str]
:rtype: List[List[str]]
"""
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        # create a hashmap for anagrams
        # the use of defaultdict() will allow us to create entries that do not exists automatically
        hashmap = defaultdict(list)

        # for each anagram in the string
        for string in strs: 
            # create an array with an index for each letter in the alphabet
            count = [0]*26
            # for each character in the string
            for char in string:
                # increment the value of the index of the letter 
                count[ord(char) - ord('a')] += 1
            # using the anagram data as a key, find its value and append the current string at the end
            # if the anagram key does not exists, it will automatically create a new entry. 
            hashmap[tuple(count)].append(string)
        # return the values of the dictionary ( a list of strings)
        return hashmap.values()
            
test = Solution()
print(test.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

