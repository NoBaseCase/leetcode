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


print(cat_dog("catdog"))

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
