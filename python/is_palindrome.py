'''
https://leetcode.com/problems/palindrome-number/

An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert the number into a string
        x_string = str(x)
        # grab length of string for readability
        length = len(x_string)
        # output of the funciton
        output = True

        # iterate through the string
        for x in range(0, length):
            # get the front and back index positions for readability
            front = x
            back = length - 1 - x
            # if back and front are equal to each other (odd numbered string)
            # or back is great than front (even numbered string), break the loop and break
            if back <= front:
                break
            else:
                # if the front does not equal the backside, set to false and break
                if x_string[front] != x_string[back]:
                    output = False
                    break
        return output

