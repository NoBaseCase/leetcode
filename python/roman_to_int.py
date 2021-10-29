'''
https://leetcode.com/problems/roman-to-integer/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        # since we need to increment x by 1 within the loop, we must create an itorator
        # if not, then x will reset after iterating within the loop.
        iterator = iter(range(0, len(s)))
        # iterate through list
        for x in iterator:
            # if there exists a dicitonary key with multiple roman numerals, add to output and skip next itoration
            if x+1 < len(s) and s[x] + s[x+1] in table:
                output += table[s[x] + s[x+1]]
                next(iterator, None)
            else:
                output += table[s[x]]
        return output


test = Solution()
print(test.romanToInt('MCMXCIV'))