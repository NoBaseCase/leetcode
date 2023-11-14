"""
Link: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

:type s: str
:type t: str
:rtype: bool
"""

""" 
time complexity: O(n)
space complexity: O(n)
"""


class Solution1(object):
    def isAnagram(self, s, t):

        # checks to make sure the strings are of the same length
        if len(s) != len(t):
            return False

        # create a list to push all the characters of string s
        list = []
        for n in s:
            list.append(n)

        # eliminating charcters from out list that are found string t
        for n in t:
            # if a character is found in string t that is not in the list, return false
            if n not in list:
                return False
            else:
                list.remove(n)
        return True


class Solution2(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        # creates two hash maps to keep track of the contents of string s and t
        count_s, count_t = {}, {}

        # iterates through both strings, adding the current character to the hash map
        # if the character does not exists, it creates a new entry, with a value of 1
        # of the character does exists, it retrieves its value and increments it by 1
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        # now we check to see if the character counts match for both hash maps for every character
        # if they do not match, return false
        for c in count_s:
            #  the .get function is used to return a default value of zero to prevent throwing a key error
            if count_s[c] != count_t.get(c, 0):    
                return False
        return True

from collections import Counter
class Solution3(object):
    def isAnagram(self, s, t):
        # Counter() returns a dictionary of the frequency of each item in the list
        # if both dictionaries match, then we have an anagram
        return Counter(s) == Counter(t)


class Solution4(object):
    def isAnagram(self, s, t):
        # sort the strings and then compare them. 
        return sorted(s) == sorted(t)


# test1 = Solution1()
# print(test1.isAnagram("act", "cat"))

# test2 = Solution2()
# print(test2.isAnagram("act", "cat"))

# test3 = Solution3()
# print(test3.isAnagram("act", "cat"))

test4 = Solution4()
print(test4.isAnagram("act", "cat"))
