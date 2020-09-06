# Author: Akshaj Verma
import math
import string
import random
from functools import reduce, partial


def fibonacci(num: int) -> "list of fibonacci numbers":
    """
    Function to calculate the fibonacci sequence.
    Input: Integer > 2
    Output: List of fibonacci numbers
    """
    first = 0
    second = 1
    fib_list = [0, 1]

    for i in range(2, num):
        current = first + second
        fib_list.append(current)
        first = second
        second = current

    return fib_list


def is_fibonacci(num: int) -> "Boolean":
    """
    Checks if a number is present in fibonaccci sequence.
    Input: Positive integer
    Output: True if given number is fib, else False.
    """
    if num < 0:
        raise ValueError("Number must be greater than 0.")
    if not isinstance(num, int):
        raise ValueError("Input number must be an integer.")

    return bool(list(filter(lambda x: x == num, fibonacci(1000))))


# Q 2.1
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

ans2_1 = [i + j for i, j in zip(a, b) if i % 2 == 0 and j % 2 != 0]

# Q2.2
a = "tsai"
vowels = ["a", "e", "i", "o", "u"]

ans2_2 = [i for i in a if i not in vowels]


# Q2.3
a = [-1, -0.9, -0.5, 0, 0.5, 0.9, 1]
ans2_3 = [i if i > 0 else 0 for i in a]


# Q2.4
a = [1, 2, 3, 4]
ans2_4 = [1 / (1 + math.exp(-i)) for i in a]


# Q2.5
inp_text = "uvwx"
ans2_5 = [
    string.ascii_lowercase[(string.ascii_lowercase.index(i) + 5) % 26] for i in inp_text
]

# Q3
with open("test_para.txt", "r") as reader:
    sample_text = reader.readlines()
    sample_text = "".join(sample_text)
    text_list = sample_text.split(" ")
    text_list = [i.lower() for i in text_list]

with open("prof_words.txt", "r") as reader:
    prof_words = reader.readlines()
    prof_words = [i[:-2].lower() for i in prof_words]


words_found = [i for i in text_list if i in prof_words]


# Q4.1
a = [1, 2, 3, 4, 5, 6, 7, 8]
even_sum = reduce(lambda i, j: i + j, filter(lambda x: x % 2 == 0, a))


# Q4.2
a = ["a", "b", "Z", "!"]
big_ascii = reduce(lambda x, y: x if ord(x) > ord(y) else y, a)


# Q4.3
a = [1, 2, 3, 4, 5, 6]
sum_third = reduce(lambda i, j: i + j, filter(lambda x: (a.index(x) + 1) % 3 == 0, a))


# Q5
number_plates = [
    f"KA{random.randint(10, 99)}{string.ascii_uppercase[random.randint(0, 25)]}{string.ascii_uppercase[random.randint(0, 25)]}{random.randint(1000, 9999)}"
    for i in range(15)
]


# Q6
def custom_number_plate(state, low, up):
    number_plates = [
        f"{state}{random.randint(10, 99)}{string.ascii_uppercase[random.randint(0, 25)]}{string.ascii_uppercase[random.randint(0, 25)]}{random.randint(low, up)}"
        for i in range(15)
    ]

    return number_plates


# Q6.1
low_lim = 1000
up_lim = 9999

partial_custom_plate = partial(custom_number_plate, low=low_lim, up=up_lim)
