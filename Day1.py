
if __name__ == '__main__':
    print(50, 6.05, 'aniket') # comma denotes spaces

    print("Hello", end=" ")
    print("World")

    """ Python Data Types
    Numbers

    Strings

    Booleans """

    print(complex(10, 20))  # Represents the complex number (10 + 20j)

    f_bool = False
    print(f_bool)

    # length of a string
    print(len("aniket"))

    # In a string, every character is given a numerical index based on its position
    batman = "Bruce Wayne"
    first = batman[0]
    print("first", first)
    last = batman[len(batman)-1]
    print("last", last)
    print(batman[-1])  # starting from last char - reverse indexing

    # String Immutability. Once we assign a value to a string, we can’t update it later.
    string = "Immutability"
    # string[0] = 'O'  # Will give error

    # when we assign a new value to str1 (at line 4) its identity changes not the value
    str1 = "hello"
    print(id(str1))

    str1 = "bye"
    print(id(str1))

    first = 10
    print(id(first))
    first = first+10
    print(id(first))

    # Python offers another data type called NoneType. It only has a single value, None.
    # We can assign None to any variable, but we can not create other NoneType variables.
    """None is not a default value for the variable that has not yet been assigned a value.
None is not the same as False.
None is not an empty string.
None is not 0. """
    val = None
    print(val)  # prints "None" and returns None
    print(type(val))

    # String Slicing
    my_string = "This is MY string!"
    print(my_string[0:4])  # From the start till before the 4th index
    print(my_string[1:7])
    print(my_string[8:len(my_string)])  # From the 8th index till the end

    my_string = "This is MY string!"
    print(my_string[0:7])  # A step of 1
    print(my_string[0:7:2])  # A step of 2
    print(my_string[0:7:5])  # A step of 5

    my_string = "This is MY string!"
    print(my_string[13:2:-1])  # Take 1 step back each time
    print(my_string[17:0:-2])  # Take 2 steps back. The opposite of what happens in the slide above

    # Partial Slicing
    my_string = "This is MY string!"
    print(my_string[:8])  # All the characters before 'M'
    print(my_string[8:])  # All the characters starting from 'M'
    print(my_string[:])  # The whole string
    print(my_string[::-1])  # The whole string in reverse (step is -1)

    # Python automatically converts the integer to a floating-point number in case of operation with float

    # Division
    float1 = 5.0
    float2 = 2.0
    print(float1 / float2)
    print(12.4 / 2)

    # Floor Division In floor division, the result is floored to the nearest smaller integer. It is also known as integer division.
    float1 = 5.6
    float2 = 2.0
    print(float1 // float2)
    print(12.4 // 2)
    print(2 // 2)

    # comparison
    num1 = 5
    num2 = 10
    num3 = 10
    list1 = [6, 7, 8]
    list2 = [6, 7, 8]

    print(num2 > num1)  # 10 is greater than 5
    print(num1 > num2)  # 5 is not greater than 10

    print(num2 == num3)  # Both have the same value
    print(num3 != num1)  # Both have different values

    print(3 + 10 == 5 + 5)  # Both are not equal
    print(3 <= 2)  # 3 is not less than or equal to 2

    print(num2 is not num3)  # Both have the same object
    print(list1 is list2)  # Both have the different objects

    # One thing to note is that when a variable, first, is assigned to another variable, second, its value is copied into second.
    # Hence, if we later change the value of first, second will remain unaffected:

    first = 20
    second = first
    first = 35  # Updating 'first'

    print(first, second)  # 'second' remains unchanged

    # Bitwise Operators
    num1 = 10  # Binary value = 01010
    num2 = 20  # Binary Value = 10100

    print(num1 & num2)  # 0   -> Binary value = 00000
    print(num1 | num2)  # 30  -> Binary value = 11110
    print(num1 ^ num2)  # 30  -> Binary value = 11110 (XOR)
    print(~num1)  # -11 -> Binary value = -(1011) (NOT)
    print(num1 << 3)  # 80  -> Binary value = 0101 0000 (Shift Bits Left)
    print(num2 >> 3)  # 2   -> Binary value = 0010 (Shift Bits Right)

    # Comparison Operators
    # Strings are compatible with the comparison operators. Each character has a Unicode value.
    # This allows strings to be compared on the basis of their Unicode values.
    # When two strings have different lengths, the string which comes first in the dictionary is said to have the smaller value.
    print('a' < 'b')  # 'a' has a smaller Unicode value
    house = "Gryffindor"
    house_copy = "Gryffindor"
    print(house is house_copy)
    new_house = "Slytherin"
    print(house == new_house)
    print(new_house <= house)
    print(new_house >= house)

    # concat
    first_half = "Bat"
    second_half = "man"
    full_name = first_half + second_half
    print(full_name)

    print("ha" * 3)

    # Search
    random_string = "This is a random string"
    print('of' not in random_string)  # Check whether 'of' exists in randomString
    print('Th' in random_string)  # 'random' exists!

    







