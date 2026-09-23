"""
===================================================================
 Python Solutions to 3 Programming Problems
 Simple, Clean, and Fully Explained
===================================================================

1. Binary Divisibility by 5
2. Letter and Digit Counter
3. Factorial of Given Numbers
"""

# ===================================================================
# Problem 1: 4-digit Binary Numbers Divisible by 5
# ===================================================================
def check_binary_divisible_by_5(binary_input: str) -> str:
    """
    Accepts comma-separated 4-digit binary strings and filters those divisible by 5.

    How it works:
    - Splits the string by comma to get individual binary strings.
    - int(binary_str, 2) converts binary string representation into base-10 integer.
    - If base-10 integer % 5 == 0, it is divisible by 5.
    - Joins the valid binary strings back with a comma.
    """
    valid_numbers = []
    for item in binary_input.split(","):
        clean_item = item.strip()
        if clean_item:
            # Convert binary (base 2) to decimal (base 10)
            decimal_value = int(clean_item, 2)
            if decimal_value % 5 == 0:
                valid_numbers.append(clean_item)
    return ",".join(valid_numbers)


# ===================================================================
# Problem 2: Count Letters and Digits in a Sentence
# ===================================================================
def count_letters_and_digits(sentence: str):
    """
    Counts letters and digits in a sentence and displays the counts.

    How it works:
    - Iterates over each character in the sentence.
    - char.isalpha() checks if the character is an alphabet letter (A-Z, a-z).
    - char.isdigit() checks if the character is a numeric digit (0-9).
    - Other characters (spaces, punctuation marks like '!') are ignored.
    """
    letters = 0
    digits = 0
    
    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
            
    return letters, digits


# ===================================================================
# Problem 3: Factorial of Given Number(s)
# ===================================================================
def calculate_factorial(n: int) -> int:
    """
    Computes factorial iteratively: n! = n * (n - 1) * ... * 1
    0! = 1 by definition.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def factorial_csv_sequence(numbers_input: str) -> str:
    """
    Accepts comma-separated number(s), computes each factorial,
    and returns them as a comma-separated single-line string.
    """
    results = []
    for item in numbers_input.split(","):
        clean_item = item.strip()
        if clean_item:
            fact = calculate_factorial(int(clean_item))
            results.append(str(fact))
    return ",".join(results)


# ===================================================================
# Demonstration / Execution
# ===================================================================
def run_all_examples():
    print("=" * 60)
    print("PROBLEM 1: Binary Divisible by 5")
    print("=" * 60)
    p1_input = "0100,0011,1010,1001"
    print(f"Input : {p1_input}")
    print(f"Output: {check_binary_divisible_by_5(p1_input)}")
    print()

    print("=" * 60)
    print("PROBLEM 2: Count Letters and Digits")
    print("=" * 60)
    p2_input = "hello world! 123"
    letters, digits = count_letters_and_digits(p2_input)
    print(f"Input : {p2_input}")
    print("Output:")
    print(f"LETTERS {letters}")
    print(f"DIGITS {digits}")
    print()

    print("=" * 60)
    print("PROBLEM 3: Factorial Calculation")
    print("=" * 60)
    p3_input = "8"
    print(f"Input : {p3_input}")
    print(f"Output: {factorial_csv_sequence(p3_input)}")
    print()


if __name__ == "__main__":
    run_all_examples()
