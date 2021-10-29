'''
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # function output
        output = ''
        # initialize the length and the smallest word to be the first
        # word in the list
        smallest_word = strs[0]
        smallest_word_length = len(strs[0])

        # finds the new smallest word and its length
        for x in strs:
            if len(x) < smallest_word_length:
                smallest_word = x
                smallest_word_length = len(x)

        # character iterater based on length of smallest word
        for letter in range(0, smallest_word_length):
            # iterates throughout list
            for word in range(0, len(strs)):
                # if current letter in string does not match smallest word
                if strs[word][letter] != smallest_word[letter]:
                    return output
            output += smallest_word[letter]
        return output
        
mylist = ['']
test = Solution()
print(test.longestCommonPrefix(mylist))