import unittest

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

class TestRomanToInt(unittest.TestCase):
    #Test fot single letter
    def test_single_letters(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("V"), 5)
        self.assertEqual(roman_to_int("X"), 10)
        self.assertEqual(roman_to_int("L"), 50)
        self.assertEqual(roman_to_int("C"), 100)
        self.assertEqual(roman_to_int("D"), 500)
        self.assertEqual(roman_to_int("M"), 1000)

    #Test for multiple value letters
    def test_many_letters(self):
        self.assertEqual(roman_to_int("XI"), 11)
        self.assertEqual(roman_to_int("XV"), 15)

    #Test for subtractive notation letters
    def test_subtractive_notation(self):
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)


    #Test fot subtractive notation
    def test_with_and_without_subtractive_notation(self):
        self.assertEqual(roman_to_int("XIV"), 14)
        self.assertEqual(roman_to_int("XIV"), 14)


    #Test for repetitive values
    def test_repetition(self):
        self.assertEqual(roman_to_int("III"), 3)
        self.assertEqual(roman_to_int("II"), 2)

    #Test for the first value
    def test_first_number(self):
        self.assertEqual(roman_to_int("I"), 1)


    #Test for an invalid value
    def test_invalid_letter(self):
        self.assertEqual(roman_to_int("Z"), "No Such Value Exists")


    #Test for an invalid with a valid value
    def test_invalid_and_valid_letter(self):
        self.assertEqual(roman_to_int("XIZ"), "No Such value Exists")


    #Test for non valid sequence of characters
    def test_not_valid(self):
        self.assertEqual(roman_to_int("VV"), "You cannot perform such an action")

    #Test for null values
    def test_null(self):
        self.assertEqual(roman_to_int(""), 0)

if __name__ == '__main__':
    unittest.main()
