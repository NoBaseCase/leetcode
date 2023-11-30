"""
Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
"""


def double_char(str):
    output = ""
    for char in str:
        output += "" + char * 2
    return output


"""
Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""


def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i : i + 2] == "hi":
            count = count + 1
    return count


"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""


def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for i in range(len(str) - 2):
        if str[i : i + 3] == "cat":
            cat_count = cat_count + 1
        if str[i : i + 3] == "dog":
            dog_count = dog_count + 1
    return cat_count == dog_count


# print(cat_dog("catdog"))

"""
Return the number of times that the string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""


def count_code(str):
    output = 0
    for i in range(len(str) - 3):
        if str[i : i + 2] == "co" and str[i + 3] == "e":
            output += 1
    return output


"""
Given two strings, return True if either of the strings appears at the very end of the other string,
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").

Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""


def end_other(a, b):
    a = a.lower()
    b = b.lower()

    if a == b:
        return True
    if len(a) < len(b):
        if b[len(b) - len(a) :] == a:
            return True
    if len(b) < len(a):
        if a[len(a) - len(b) :] == b:
            return True
    return False


"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not.


xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""


def xyz_there(str):
    if len(str) < 3:
        return False
    elif str == "xyz":
        return True
    else:
        for i in range(len(str) - 2):
            if str[i : i + 3] == "xyz":
                if str[i - 1] != ".":
                    return True
    return False


"""
Return the number of even ints in the given array. 
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""


def count_evens(nums):
    even_nums = 0
    for num in nums:
        if num % 2 == 0:
            even_nums += 1
    return even_nums


"""
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""


def big_diff(nums):
    if len(nums) == 1:
        return 0
    elif len(nums) == 2:
        return abs(nums[0] - nums[1])
    else:
        min = nums[0]
        max = nums[0]
        for num in nums:
            if num < min:
                min = num
            if num > max:
                max = num
        return abs(max - min)


"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array.
If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value.

Use int division to produce the final average. You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""


def centered_average(nums):
    min = nums[0]
    max = nums[0]
    total = 0
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
        if nums[i] > max:
            max = nums[i]

    for num in nums:
        total = total + num
    total = (total - (max + min)) / (len(nums) - 2)
    return total


"""
Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""


def sum13(nums):
    sum = 0
    if len(nums) == 0:
        return sum
    index = 0
    while index < len(nums):
        if nums[index] == 13:
            index = index + 2
        else:
            sum += nums[index]
            index = index + 1
    return sum


"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7
(every 6 will be followed by at least one 7).

Return 0 for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""


def sum67(nums):
    index = 0
    flag = False
    sum = 0

    while index < len(nums):
        if nums[index] == 6:
            flag = True
        elif flag and nums[index] == 7:
            flag = False
        elif flag:
            pass
        else:
            sum += nums[index]
        index = index + 1
    return sum


"""
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""


def has22(nums):
    if len(nums) < 2:
        return False
    for i in range(len(nums)):
        if nums[i] == 2:
            if i == len(nums) - 1:
                break
            elif nums[i + 1] == 2:
                return True
    return False
