"""
#conditions :

#1 if statement
a=10
if a>5:
    print("a is greater than 5")

#2 if-else statement
b=3
if b%2==0:
    print("b is even")
else:
    print("b is odd")
    
#eg : 
money = int(input("please give money for icecream :"))
if money == 10:
    print("i will get orange bite icecream")
else:
    print("i will not get icecream")
    
#3 if-elif-else statement
c=15
if c>0:
    print("c is positive")
elif c<0:
    print("c is negative")
else:
    print("c is zero")

#eg : real life example
marks = int(input("enter your marks : "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
    
#4 nested if statement
d=25
if d>0:
    if d%2==0:
        print("d is a positive even number")
    else:
        print("d is a positive odd number")
else:
    print("d is not a positive number")

num1 = int(input("pehla number bol bhai : "))
num2 = int(input("abb dusra bhi bol de : "))

if num1>num2:
    print(f"{num1} bada hai {num2} se bhai.")
elif num2>num1:
    print(f"{num2} bada hai {num1} se bhai.")
else:
    print("dono barabar hain bhai.")
    
#q1
print("=============ticket price based on gender==============")
gender = str(input("enter your gender (male/female) : "))

if gender == "male":
    print(f"you have to pay 100rs for ticket")
elif gender == "female":
    print(f"you have to pay 50rs for ticket")
else:
    print("invalid input")
    
#q2
print("=============check if a number is divisible by 3 and 5==============")
number = int(input("Enter the Number : "))

if number%3==0 and number%5==0:
    print(f"{number} is divisible by both 3 and 5")
else:
    print(f"{number} is not divisible by both 3 and 5")
    

print("=============Valid Voter Check============")

name = str(input("Enter you correct Name as per Addhar Card : "))
Age = int(input("Enter your Age : " ))
if Age>=18:
    print(f"🥳 Congratulations {name}, you are eligible to vote!")
else:
    print(f"😔 Sorry {name}, you are not eligible to vote yet.")
    


#q3
print("=============Find the largest among three numbers==============")
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")

#q4
print("=============Check if a year is a leap year==============")
year = int(input("Saal daalo bhai : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} leap year hai bhai.")
else:
    print(f"{year} leap year nahi hai bhai.")

"""

#q5
print("🌡️🌡️🌡️  BHOJPURI TEMPERATURE MACHINE  🌡️🌡️🌡️")
print("Are bhaiya temperature batao, hum mood bata dete hain 😄\n")

temp = float(input("🌞 Celsius me temperature daalo bhai: "))

if temp < 0:
    print("🥶❄️ Barfili Thand!")
    print("Are bap re! Freezer me ghus gaye ka bhai? Rajai odho, chai piyo ☕🧥")

elif temp <= 10:
    print("🥶 Bahut Thand!")
    print("Hawa kaat rahi hai bhai… sweater nikaal lo 🧣😬")

elif temp <= 20:
    print("🧥 Thanda-Thanda Mausam!")
    print("Chai + pakode = zindagi ka sukh 😋☕")

elif temp <= 30:
    print("😌☁️ Suhana Mausam!")
    print("Na AC chahiye, na heater… full setting hai bhai 🌿")

elif temp <= 40:
    print("🔥 Garam-Garam!")
    print("AC chalao, paani piyo, zyada hero mat bano 😓🥤")

else:
    print("☀️🔥 Bahut Zyada Garami!")
    print("Are bhaiya! Suraj seedha khopdi pe baith gaya hai 🌞😵")
