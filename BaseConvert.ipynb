import string
import re

# Split a word into its characters
def split(word):
    return list(word)

# Convert a list to a string
def list_to_string(lst):
    return ''.join(map(str, lst))

# Insert commas into a number string for thousands separators
def insert_commas(num):
    num = int(num)
    is_negative = num < 0
    num = abs(num)
    num_str = str(num)[::-1]
    result = ','.join(num_str[i:i + 3] for i in range(0, len(num_str), 3))[::-1]
    return f"-{result}" if is_negative else result

# Remove commas from all elements of a list
def remove_commas(main_list):
    return [str(item).replace(',', '') for item in main_list]

# Check if a character is valid in a given base
def is_valid_char_in_base(char):
    valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return char in valid_chars

# Extract contiguous numeric characters or numbers in parentheses from a string
def extract_numbers(string):
    # Use regex to extract numbers and numbers within parentheses
    numbers = re.findall(r'\d+|\([^\)]+\)', string)
    # Remove parentheses and convert to numbers
    numbers = [num.strip('()') for num in numbers]
    return numbers

# Convert a number to a list of digits in a specific base
def number_to_base_list(n, base):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return digits[::-1]

LETTERS = list(string.ascii_uppercase)

# Convert numeric values above 9 to their corresponding letters
def convert_to_letters(num_list, base):
    result = ''
    for digit in num_list:
        if digit >= 36:
            result += f'({digit})'
        elif digit >= 10:
            result += LETTERS[digit - 10]
        else:
            result += str(digit)
    return result

# Reverse process to convert letters back to numbers
def letters_to_numbers(my_string):
    result = []
    index = 0
    while index < len(my_string):
        if my_string[index] == '(':
            end_index = my_string.find(')', index)
            if end_index == -1:
                raise ValueError("Mismatched parentheses in input.")
            num = int(my_string[index+1:end_index])
            result.append(num)
            index = end_index + 1
        elif my_string[index].isdigit():
            result.append(int(my_string[index]))
            index += 1
        elif my_string[index].isalpha():
            result.append(LETTERS.index(my_string[index].upper()) + 10)
            index += 1
        else:
            index += 1  # Skip any other characters
    return result

# Convert a list of digits to base 10
def to_base_10(digits, base):
    return sum(int(digit) * (base ** (len(digits) - index - 1)) for index, digit in enumerate(digits))

# Generate a string representation of a number in base 10
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

def to_base_10_view(digits, base):
    terms = []
    for index, digit in enumerate(digits):
        exponent = len(digits) - index - 1
        term = f"{digit}·{base}{str(exponent).translate(SUP)}"
        terms.append(term)
    return ' + '.join(terms)

# Main function to convert between bases
def base_converter():
    input_number = input("Enter the number to be converted: ")
    input_base = int(input("Enter the base of the input number: "))
    target_base = int(input("Enter the base you want to convert to: "))

    try:
        if '(' in input_number:
            number_list = [int(num) for num in extract_numbers(input_number)]
        else:
            number_list = letters_to_numbers(input_number)
    except ValueError as e:
        print(f"Invalid input format: {e}")
        return

    base_10_number = to_base_10(number_list, input_base)

    print(f"\n\nOur first step is to convert the number {input_number} to base 10.")
    print(f"\nThis equals: {to_base_10_view(number_list, input_base)}")
    print(f"\nThis gives us: {insert_commas(base_10_number)}")

    converted_list = number_to_base_list(base_10_number, target_base)
    converted_result = convert_to_letters(converted_list, target_base)

    print(f"\n\nThe number {input_number} in base {input_base} converted to base {target_base} is: {converted_result}")

# Run the converter
if __name__ == "__main__":
    base_converter()
