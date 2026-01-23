'''
#datatypes
#int : Integer datatype eg. 12, -5, 0
a=12
print(type(a))

#float : Decimal point datatype eg. 5.9, -2.3, 0.0
b = 12/3 # float division
print(type(b))

#complex : Complex number datatype eg. 2+3j, -1+0.5j
c = 2 + 3j
print(type(c))
#string : Sequence of characters datatype eg. "hello", 'a', """This is a string"""
str = 'jiasndjc 128390182 @#$%^&*()'
str1 = "Hello, World!"
print(type(str))

#boolean : True or False datatype
bool1 = True
print(type(bool1))

# ord and chr functions
a="A"
print(ord(a))  # ord() function returns the ASCII value of a character

b=65
print(chr(b))  # chr() function returns the character corresponding to an ASCII value

# ord converts the char to its ASCII value , and chr converts the ASCII value to its char

#string takes more memory than int and float because it stores multiple characters and also the unicode values for each character

#indexing in string
a="hello brother"
#starting index = 0
#ending index = length-1
#negative indexing starts from -1 at the end of the string

print(a[0])  #h
print(a[4])  #o
#print(a[15]) #error index out of range
print(a[-1], a[5])


#string slicing
b="Hello, welcome to the world of Python programming"
print(b[0:5])  #Hello
a="hello"

a[1:4:1]  #ell
#start : end : step

#skipping characters
print((a[0:6:2]))   #hlo

#from start
print(a[:4])  #hell

#till end
print(a[2:])  #llo

#reverse string
print(a[::-1])  #olleh

'''


#type conversion
