import unittest,pytest
newmap = {"I": 1 , "V":5, "X":10,"L":50, "C":100, "D":500,"M":1000}


def roman_to_int(s):
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and newmap[s[i]] < newmap[s[i+1]]:
            result -= newmap[s[i]]
        else:
            result += newmap[s[i]]
    if result == -1 :
        return "No Such value Exists"
    return result




def test_empty_string():
    assert roman_to_int("") == 0


def test_single_character():
    assert roman_to_int("I") == 1
    assert roman_to_int("V") == 5
    assert roman_to_int("X") == 10


def test_multiple_characters():
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("XLIX") == 49


def test_complex_cases():
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("MDXL") == 1540


def test_invalid_characters():
    with pytest.raises(ValueError):
        roman_to_int("IIII")
    with pytest.raises(ValueError):
        roman_to_int("VV")
    with pytest.raises(ValueError):
        roman_to_int("LL")


if __name__ == "__main__":
    print(roman_to_int("MCMXCV"))  # Output: 1995
    test_empty_string()
    test_single_character()
    test_multiple_characters()
    test_complex_cases()
   # test_invalid_characters()

