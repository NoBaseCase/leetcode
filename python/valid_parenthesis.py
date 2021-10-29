'''
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2:
            return False
        else:
            # iterate through string
            for index in range(0, len(s)):
                print(stack)
                if s[index] =='(' or s[index] == '[' or s[index] == '{':
                    stack.append(s[index])
                else:
                    if not stack and (s[index] ==')' or s[index] == ']' or s[index] == '}'):
                        return False
                    elif s[index] == ')' and stack[-1] == '(':
                        stack.pop()
                    elif s[index] == ']' and stack[-1] == '[':
                        stack.pop()
                    elif s[index] == '}' and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
            if stack:
                return False
            return True
test = Solution()
print(test.isValid("(){}}{"))