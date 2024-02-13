import unittest


# function to store the basic roman symbols
def map_symbols(s):
    if s == "I":
        return 1
    if s == "V":
        return 5
    if s == "X":
        return 10
    if s == "L":
        return 50
    if s == "C":
        return 100
    if s == "D":
        return 500
    if s == "M":
        return 1000
    return -1



def change_roman_to_int(roman):
    if "I" or "V" or "X" or "L"  or "C"  or "C" or "D" or "M" not in roman:
         print("Invalid Output")
    if roman.count("V") > 1:
        print("Invalid Output")
    elif roman.count("L") > 1:
        print("Invalid Output")
    elif roman.count("C") > 3:
        print("Invalid Output")
    elif roman.count("M") > 3:
        print("Invalid Output")
    elif roman.count("I") > 3:
        print("Invalid Output")
    elif roman.count("X") > 3:
        print("Invalid Output")
    else: 
        ans = 0
        i = 0

        while i < len(roman):
            x1 = map_symbols(roman[i])

            if i + 1 < len(roman):
                x2 = map_symbols(roman[i + 1])
                
                if x1 >= x2:
                    ans = ans + x1
                    i = i + 1
                else:
                    ans = ans + x2 - x1
                    i = i + 2
                
            else:
                ans = ans + x1
                i = i + 1

        if ans == -1 :
            return "No Such value Exists"
        else:
            return ans



# driver code
r = input("Enter the roman numeral: ").upper()
print("The integer equivalent is: ")
print(change_roman_to_int(r))