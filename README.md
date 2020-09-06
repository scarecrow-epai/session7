#Session 7

This is the readme for session-7.
This file contains information for functions present in `session7.py` and `test_session7.py`.

## Run Tests 

```
pytest -v  
```


## Functions in `session7.py`.


 The function definitions are as follows: 

### fibonacci(num: int) -> "list of fibonacci numbers"


    Function to calculate the fibonacci sequence.

### is_fibonacci(num: int) -> "Boolean"


    Checks if a number is present in fibonaccci sequence.

### custom_number_plate(state, low, up)


        f"{state}{random.randint(10, 99)}{string.ascii_uppercase[random.randint(0, 25)]}{string.ascii_uppercase[random.randint(0, 25)]}{random.randint(low, up)}"


## Functions in `test_session7.py`.


The test definitions are as follows: 

### test_readme_exists()


    Test funtion to check if README exists.

### test_readme_contents()


    Test if README contains atleast 200 words.

### test_readme_proper_description()


    Check if README contains required functions..

### test_readme_file_for_formatting()


    Test function to check README file formatting.

### test_indentations()


    Returns pass if used four spaces for each level of syntactically \

### test_function_name_had_cap_letter()


    Test function to check if any function names have any capital letters.

### test_is_fibonacci()


    Function to test if a number belongs to a fibo seq.

### test_even_odd_iterable_sum()


    Test for Q2.1. Adds numbers from two iterables based on even odd condition.

### test_remove_vowels()


    Test for Q2.2. Remove vowels from a string.

### test_relu()


    Test for Q2.3. Add ReLU to a list of numbers.

### test_sigmoid()


    Test for Q2.4. Add Sigmoid to a list of numbers.

### test_ascii_shift()


    Test for Q2.5. Shift all chars in a string by 5.

### test_profanity()


    Tst for Q3. Looks for profanity in a given paragraph.gtgt

### test_even_sum()


    Test for Q4.1. Sum even numbers using reduce.

### test_biggest_ascii()


    Test for Q4.2. Find biggest ascii element in a list.

### test_sum_third()


    Test for Q4.3. Sum every 3rd element in a list

### test_number_plates_pt1()


    Test for Q6. Number plate generation.

### test_number_plates_pt2()


    Test for Q6 pt2. Number plates using partial function.

