"""
Link: https://leetcode.com/problems/palindrome-number/submissions/

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]


test = Solution()
print(test.isPalindrome(-101))

""" 
----- ANALYSIS -----
Convert the integer into a string and reverse it. if its a palindrome, then the string will check out. Since negative sings are taken
into consideration (and there exists no number where a negative sign can be on the right), the logic will hold true
"""
