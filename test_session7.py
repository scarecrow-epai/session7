import re
import os
import math
import pytest
import inspect
import session7
import string
import random
from functools import reduce

README_CONTENT_CHECK_FOR = [
    "fibonacci",
    "is_fibonacci",
    "custom_number_plate",
]


def test_readme_exists():
    """
    Test funtion to check if README exists.
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test if README contains atleast 200 words.
    """
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert (
        len(readme_words) >= 100
    ), "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    """
    Check if README contains required functions..
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass

    assert (
        READMELOOKSGOOD == True
    ), "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    """
    Test function to check README file formatting.
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    """ 
    Returns pass if used four spaces for each level of syntactically \
    significant indenting.
    """
    lines = inspect.getsource(session7)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    """
    Test function to check if any function names have any capital letters.
    """
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_is_fibonacci():
    """
    Function to test if a number belongs to a fibo seq.
    """
    assert session7.is_fibonacci(1) == True and session7.is_fibonacci(4) == False


def test_even_odd_iterable_sum():
    """
    Test for Q2.1. Adds numbers from two iterables based on even odd condition.
    """
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    assert [i + j for i, j in zip(a, b) if i % 2 == 0 and j % 2 != 0] == [9, 13]


def test_remove_vowels():
    """
    Test for Q2.2. Remove vowels from a string.
    """
    vowels = ["a", "e", "i", "o", "u"]
    assert [i for i in "tsai" if i not in vowels] == ["t", "s"]


def test_relu():
    """
    Test for Q2.3. Add ReLU to a list of numbers.
    """

    a = [-1, -0.9, -0.5, 0, 0.5, 0.9, 1]
    assert [i if i > 0 else 0 for i in a] == [0, 0, 0, 0, 0.5, 0.9, 1]


def test_sigmoid():
    """
    Test for Q2.4. Add Sigmoid to a list of numbers.
    """
    a = [1, 2, 3, 4]

    assert [1 / (1 + math.exp(-i)) for i in a] == [
        0.7310585786300049,
        0.8807970779778823,
        0.9525741268224334,
        0.9820137900379085,
    ]


def test_ascii_shift():
    """
    Test for Q2.5. Shift all chars in a string by 5.
    """
    inp_text = "uvwx"
    ans2_5 = [
        string.ascii_lowercase[(string.ascii_lowercase.index(i) + 5) % 26]
        for i in inp_text
    ]

    ans2_5 == ["z", "a", "b", "c"]


def test_profanity():
    """
    Tst for Q3. Looks for profanity in a given paragraph.gtgt
    """
    with open("test_para.txt", "r") as reader:
        sample_text = reader.readlines()
        sample_text = "".join(sample_text)
        text_list = sample_text.split(" ")
        text_list = [i.lower() for i in text_list]

    with open("prof_words.txt", "r") as reader:
        prof_words = reader.readlines()
        prof_words = [i[:-2].lower() for i in prof_words]

    assert [i for i in text_list if i in prof_words] == ["pricks", "tw4"]


def test_even_sum():
    """
    Test for Q4.1. Sum even numbers using reduce.
    """
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    assert reduce(lambda i, j: i + j, filter(lambda x: x % 2 == 0, a)) == 20


def test_biggest_ascii():
    """
    Test for Q4.2. Find biggest ascii element in a list.
    """
    a = ["a", "b", "Z", "!"]
    assert reduce(lambda x, y: x if ord(x) > ord(y) else y, a) == "b"


def test_sum_third():
    """
    Test for Q4.3. Sum every 3rd element in a list
    """

    a = [1, 2, 3, 4, 5, 6]
    assert (
        reduce(lambda i, j: i + j, filter(lambda x: (a.index(x) + 1) % 3 == 0, a)) == 9
    )


def test_number_plates_pt1():
    """
    Test for Q6. Number plate generation.
    """

    number_plates = [
        f"KA{random.randint(10, 99)}{string.ascii_uppercase[random.randint(0, 25)]}{string.ascii_uppercase[random.randint(0, 25)]}{random.randint(1000, 9999)}"
        for i in range(15)
    ]

    assert len(number_plates) == 15


def test_number_plates_pt2():
    """
    Test for Q6 pt2. Number plates using partial function.
    """

    temp = session7.partial_custom_plate("MH")
    assert len(temp) == 15 and temp[0][:2] == "MH"
