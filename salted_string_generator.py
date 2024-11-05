import random
import string

def concatenate_random_chars(input_string, num_chars=5):
    """Concatenates random numbers and special characters to an input string.

    Args:
        input_string: The input string to be modified.
        num_chars: The number of random characters to add.

    Returns:
        The modified string with random characters appended.
    """

    # Define a string of characters to choose from
    chars = string.digits + string.punctuation

    # Generate random characters
    random_chars = ''.join(random.choice(chars) for _ in range(num_chars))

    # Concatenate the random characters to the input string
    modified_string = input_string + random_chars

    return modified_string

if __name__ == "__main__":
    input_str = input("Enter your string: ")
    result_str = concatenate_random_chars(input_str)
    print("Modified string:", result_str)