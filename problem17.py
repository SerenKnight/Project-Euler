num_and_letters = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}


def count_letters_in_number(number):
    digits = 0
    if 0 <= number <= 20:
        digits += len(num_and_letters[number])
    elif 21 <= number <= 99:
        if number % 10 == 0:
            digits += len(num_and_letters[number])
        else:
            first_digit = int(str(number)[0]) * 10
            second_digit = int(str(number)[1])
            digits += len(num_and_letters[first_digit])
            digits += len(num_and_letters[second_digit])
    elif 100 <= number <= 999:
        if number % 100 == 0:
            digits += len(num_and_letters[number / 100])
            digits += len(num_and_letters[100])
        else:
            first_digit = int(str(number)[0])
            digits += len(num_and_letters[first_digit])
            digits += len(num_and_letters[100])
            digits += 3
            number - first_digit * 100
    elif 1000 <= number <= 9999:
        if number % 1000 == 0:
            digits += len(num_and_letters[number / 1000])
            digits += len(num_and_letters[1000])
        else:
            first_digit = int(str(number)[0]) * 1000
            digits += len(num_and_letters[first_digit])
            digits += len(num_and_letters[1000])
            digits += 3
            number - first_digit * 1000
    return digits


def number_letter_counts(a, b):
    digits = 0
    for numbers in range(a, b + 1):
        count = 0
        count += count_letters_in_number(numbers)
        print(count)


number_letter_counts(115, 116)

print(count_letters_in_number(115))
