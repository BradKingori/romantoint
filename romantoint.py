import pytest

newmap = {"I": 1 , "V":5, "X":10,"L":50, "C":100, "D":500,"M":1000}

def roman_to_int(s):
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and newmap[s[i]] < newmap[s[i+1]]:
            result -= newmap[s[i]]
        else:
            result += newmap[s[i]]
    if result == -1:
        return "No Such value Exists"
    return result

# Test for single letter
def test_single_letters():
    assert roman_to_int("I") == 1
    assert roman_to_int("V") == 5
    assert roman_to_int("X") == 10
    assert roman_to_int("L") == 50
    assert roman_to_int("C") == 100
    assert roman_to_int("D") == 500
    assert roman_to_int("M") == 1000

# Test for multiple value letters
def test_many_letters():
    assert roman_to_int("XI") == 11
    assert roman_to_int("XV") == 15

# Test for subtractive notation letters
def test_subtractive_notation():
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9

# Test for subtractive notation
def test_with_and_without_subtractive_notation():
    assert roman_to_int("XIV") == 14
    assert roman_to_int("XIX") == 19

# Test for repetitive values
def test_repetition():
    assert roman_to_int("III") == 3
    assert roman_to_int("II") == 2

# Test for the first value
def test_first_number():
    assert roman_to_int("I") == 1

# Test for an invalid value
def test_invalid_letter():
    assert roman_to_int("Z") == "No Such Value Exists"

# Test for an invalid with a valid value
def test_invalid_and_valid_letter():
    assert roman_to_int("XIZ") == "No Such value Exists"

# Test for non valid sequence of characters
def test_not_valid():
    assert roman_to_int("VV") == "You cannot perform such an action"

# Test for null values
def test_null():
    assert roman_to_int("") == 0

# The primary code to run the application
#def romantointmain():
#    roman_numeral = input("Enter a Roman numeral: ").upper()
#    result = roman_to_int(roman_numeral)
#    print(f"The integer value of {roman_numeral} is: {result}")

#if __name__ == "__main__":
#    romantointmain()

