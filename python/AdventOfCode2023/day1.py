import os

"""
----- PART 1 -----
converts a string with numbers embedded inside it into a single integer digit.
Wil strip only the First and last number embedded in the string. If only one digit is present, then it will return 
the single digit twice.  
"""


def strip_number(str):
    first_digit = ""
    second_digit = ""
    for char in str:
        if not char.isalpha():
            if first_digit == "":
                first_digit = char
            else:
                second_digit = char
    if second_digit == "":
        return int(first_digit + first_digit)
    return int(first_digit + second_digit)


sum = 0
with open("input.txt", "r") as file:
    line = file.read().splitlines()
    for item in line:
        sum += strip_number(item)
    print(sum)


"""
----- PART 2 -----

I solved the problems utilizing a dictionary that contain both the word and numerical representations of a number. I use the dictionary
to check string permutations and see if i find a match. Start by looking for the first digit on the left hand side of the string, 
moving towards the right as i search for either a number or a word that represents a number. then i repeat the exact process,
but with the left hand side respectively. Once We have both digits, we combine them and convert them into an integer and add them to 
the sum.
"""

valid_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_number(input):
    output = ""
    for i in range(len(input)):
        # character representation of numbers can only be 3 4 or 5 letters
        three_letter_num = input[i : i + 3]
        four_letter_num = input[i : i + 4]
        five_letter_num = input[i : i + 5]

        # integer representation of values are shorter therefore have higher priority to check for when iterating
        # through a string
        if not input[i].isalpha():
            output = input[i]
            break
        # if a valid number is found, retrieve its integer character, and end the loop
        if three_letter_num in valid_numbers:
            output = valid_numbers[three_letter_num]
            break
        if four_letter_num in valid_numbers:
            output = valid_numbers[four_letter_num]
            break
        if five_letter_num in valid_numbers:
            output = valid_numbers[five_letter_num]
            break
    return output


def get_second_number(input):
    # since the second digit is the rightmost valid number, we reverse the string to start at the back
    input = input[::-1]
    output = ""
    for i in range(len(input)):
        three_letter_num = input[i : i + 3]
        # since the string is reverse, so will be the substrings that we obtain,
        # so we must unreverse those to perform valid lookups
        three_letter_num = three_letter_num[::-1]

        four_letter_num = input[i : i + 4]
        four_letter_num = four_letter_num[::-1]

        five_letter_num = input[i : i + 5]
        five_letter_num = five_letter_num[::-1]

        if not input[i].isalpha():
            output = input[i]
            break
        if three_letter_num in valid_numbers:
            output = valid_numbers[three_letter_num]
            break
        if four_letter_num in valid_numbers:
            output = valid_numbers[four_letter_num]
            break
        if five_letter_num in valid_numbers:
            output = valid_numbers[five_letter_num]
            break
    return output


sum = 0
with open("input.txt", "r") as file:
    line = file.read().splitlines()
    for item in line:
        first_digit = get_first_number(item)
        second_digit = get_second_number(item)
        final_digit = int(first_digit + second_digit)
        sum = sum + final_digit
    print(sum)
