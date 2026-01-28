""""
a = 5
b = 10
addition = a + b
print("Addition:", addition)  # Addition: 15
substraction = b - a
print("Substraction:", substraction)  # Substraction: 5
multiplication = a * b
print("Multiplication:", multiplication)  # Multiplication: 50
division = b / a
print("Division:", division)  # Division: 2.0
modulus = b % a
print("Modulus:", modulus)  # Modulus: 0
floor_division = b // a
print("Floor Division:", floor_division)  # Floor Division: 2
exponentiation = a ** 2
print("Exponentiation:", exponentiation)  # Exponentiation: 25


# Comparison Operators
x = 15
y = 10
print("Equal:", x == y)  # Equal: False
print("Not Equal:", x != y)  # Not Equal: True
print("Greater Than:", x > y)  # Greater Than: True
print("Less Than:", x < y)  # Less Than: False
print("Greater Than or Equal To:", x >= y)  # Greater Than or Equal To: True
print("Less Than or Equal To:", x <= y)  # Less Than or Equal To: False


# Logical Operators 
p = True
q = False
print("Logical AND:", p and q)  # Logical AND: False
print("Logical OR:", p or q)  # Logical OR: True
print("Logical NOT:", not p)  # Logical NOT: False


# Assignment Operators
c = 20
c += 5
print("c after += 5:", c)  # c after += 5: 25
c *= 2
print("c after *= 2:", c)  # c after *= 2: 50
c -= 10
print("c after -= 10:", c)  # c after -= 10: 40
c /= 4
print("c after /= 4:", c)  # c after /= 4: 10.0
c %= 3
print("c after %= 3:", c)  # c after %= 3: 1.0
c **= 3
print("c after **= 3:", c)  # c after **= 3: 1.0
c //= 2
print("c after //= 2:", c)  # c after //= 2: 0.0


# Bitwise Operators
m = 5  # Binary: 0101
n = 3  # Binary: 0011
print("Bitwise AND:", m & n)  # Bitwise AND: 1 (Binary: 0001)
print("Bitwise OR:", m | n)  # Bitwise OR: 7 (Binary: 0111)
print("Bitwise XOR:", m ^ n)  # Bitwise XOR: 6 (Binary: 0110)
print("Bitwise NOT:", ~m)  # Bitwise NOT: -6 (Binary: ...1010)
print("Left Shift m by 1:", m << 1)  # Left Shift m by 1: 10 (Binary: 1010)
print("Right Shift m by 1:", m >> 1)  # Right Shift m by 1: 2 (Binary: 0010)


# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?:", 3 in my_list)  # Is 3 in my_list?: True
print("Is 6 not in my_list?:", 6 not in my_list)  # Is 6 not in my_list?: True
# Identity Operators
a = [1, 2, 3]
b = a
print("a is b:", a is b)  # a is b: True
c = a.copy()
print("a is c:", a is c)  # a is c: False
print("a == c:", a == c)  # a == c: True
print("a is not c:", a is not c)  # a is not c: True


# Operator Precedence
result = 5 + 3 * 2  # Multiplication has higher precedence than addition
print("Result of 5 + 3 * 2:", result)  # Result of 5 + 3 * 2: 11
result = (5 + 3) * 2  # Parentheses change the precedence
print("Result of (5 + 3) * 2:", result)  # Result of (5 + 3) * 2: 16


# Chained Comparisons
x = 10
print("5 < x < 15:", 5 < x < 15)  # 5 < x < 15: True
print("x > 5 >= 10:", x > 5 >= 10)  # x > 5 >= 10: True
print("x < 5 or x > 15:", x < 5 or x > 15)  # x < 5 or x > 15: False
print(type(c))  #int
print(type(float))  #float
print(type(complex))  #complex
print(type(str))  #string
print(type(bool))  #boolean
print(type(list))  #list
print(type(tuple))  #tuple
print(type(dict))  #dictionary
print(type(set))  #set
print(type(frozenset))  #frozenset
print(type(bytes))  #bytes
print(type(bytearray))  #bytearray
print(type(range))  #range
print(type(None))  #NoneType
# int : Integer datatype eg. -1, 0, 1, 2, 100
a = -100
print(type(a))  # <class 'int'>
# float : Decimal point datatype eg. 5.9, -2.3, 0.0
b = 5.9
print(type(b))  # <class 'float'>
"""

#question :
#q1
num1 = 126
num2 = 130
print("Is number 1 greater than number 2?:", num1 > num2)
print("Is number 1 less than or equal to number 2?:", num1 <= num2)
#conclusion : logical operators give boolean output True or False based on the condition provided

num3 = 15
num4 = 15
num5 = 8
num6 = 2
print((num3 == num4) != (num5 == num6)) # True : num3 equals num4 is True , num5 equals num6 is False , True != False = True

