print("😎😎😎  PYTHON CONDITIONS – FULL CHILL MODE  😎😎😎\n")

# ===================== 1. IF STATEMENT =====================
print("👉 Example 1: Simple IF")

a = 10
if a > 5:
    print("✅ Bhai a toh 5 se bada hi hai 😄\n")


# ===================== 2. IF-ELSE STATEMENT =====================
print("👉 Example 2: IF-ELSE")

b = 3
if b % 2 == 0:
    print("🔢 b even hai bhai")
else:
    print("🔢 b odd hai bhai 😎\n")


# ===================== REAL LIFE EXAMPLE =====================
print("🍦 Ice Cream Wala Scene 🍦")

money = int(input("💰 Bhai icecream ke liye paisa daal: "))

if money == 10:
    print("🍊 Orange Bite milegi bhai, partyyy 🥳\n")
else:
    print("😢 Paisa kam hai bhai, icecream cancelled\n")


# ===================== 3. IF-ELIF-ELSE =====================
print("👉 Example 3: IF-ELIF-ELSE")

c = 15
if c > 0:
    print("➕ c positive hai bhai")
elif c < 0:
    print("➖ c negative hai bhai")
else:
    print("⭕ c zero hai bhai\n")


# ===================== MARKS GRADING =====================
print("📊 Result Time Bhai 📊")

marks = int(input("📝 Apna marks daal bhai: "))

if marks >= 90:
    print("🏆 Grade A – Topper nikle ho bhai 😎")
elif marks >= 80:
    print("🥈 Grade B – Mast performance 👍")
elif marks >= 70:
    print("🥉 Grade C – Theek thaak bhai")
elif marks >= 60:
    print("🙂 Grade D – Pass ho gaye bhai")
else:
    print("😢 Grade F – Agli baar phod dena bhai\n")


# ===================== 4. NESTED IF =====================
print("👉 Example 4: Nested IF")

d = 25
if d > 0:
    if d % 2 == 0:
        print("➕ d positive aur even hai bhai")
    else:
        print("➕ d positive aur odd hai bhai")
else:
    print("❌ d positive nahi hai bhai\n")


# ===================== COMPARING TWO NUMBERS =====================
print("🔢 Do Number Ka Muqabla 🔢")

num1 = int(input("🥇 Pehla number bol bhai: "))
num2 = int(input("🥈 Dusra number bhi bol de: "))

if num1 > num2:
    print(f"😎 {num1} bada hai {num2} se bhai")
elif num2 > num1:
    print(f"😎 {num2} bada hai {num1} se bhai")
else:
    print("🤝 Dono number barabar hain bhai\n")


# ===================== Q1: TICKET PRICE =====================
print("🎟️ Ticket Price Check 🎟️")

gender = input("🧑‍🦱 Gender daal bhai (male/female): ").lower()

if gender == "male":
    print("💸 Bhai 100 rupaye dena padega")
elif gender == "female":
    print("💸 Sirf 50 rupaye, discount mila 😄")
else:
    print("❌ Galat input bhai\n")


# ===================== Q2: DIVISIBLE CHECK =====================
print("🔢 Divisible Check 🔢")

number = int(input("📌 Ek number daal bhai: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"✅ {number} 3 aur 5 dono se divisible hai bhai\n")
else:
    print(f"❌ {number} dono se divisible nahi hai bhai\n")


# ===================== VOTER CHECK =====================
print("🗳️ Voter Eligibility Check 🗳️")

name = input("🧑 Naam daal bhai (Aadhar wala): ")
age = int(input("🎂 Age bhi bol de bhai: "))

if age >= 18:
    print(f"🥳 Congrats {name}, vote daal sakte ho bhai!")
else:
    print(f"😔 Sorry {name}, abhi wait karna padega bhai\n")


# ===================== Q3: LARGEST OF THREE =====================
print("🔢 Teen Number Ka Don 🔢")

x = int(input("1️⃣ Pehla number: "))
y = int(input("2️⃣ Dusra number: "))
z = int(input("3️⃣ Teesra number: "))

if x >= y and x >= z:
    print(f"🏆 {x} sabse bada bhai")
elif y >= x and y >= z:
    print(f"🏆 {y} sabse bada bhai")
else:
    print(f"🏆 {z} sabse bada bhai\n")


# ===================== Q4: LEAP YEAR =====================
print("📅 Leap Year Check 📅")

year = int(input("📆 Saal daal bhai: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"✅ {year} leap year hai bhai 🥳")
else:
    print(f"❌ {year} leap year nahi hai bhai\n")


# ===================== Q5: TEMPERATURE MACHINE =====================
print("🌡️🌡️🌡️  DESI TEMPERATURE MACHINE  🌡️🌡️🌡️")
print("Are bhai temperature batao, hum mood bata dete hain 😄\n")

temp = float(input("🌞 Celsius me temperature daal bhai: "))

if temp < 0:
    print("🥶❄️ Barfili thand!")
    print("Rajai + chai = life ☕🧥")

elif temp <= 10:
    print("🥶 Bahut thand!")
    print("Sweater nikaal lo bhai 🧣")

elif temp <= 20:
    print("🧥 Thanda-thanda mausam")
    print("Chai + pakode best 😋")

elif temp <= 30:
    print("😌 Suhana mausam")
    print("Perfect weather bhai 🌿")

elif temp <= 40:
    print("🔥 Garam-garam!")
    print("AC chalao, paani piyo 😓")

else:
    print("☀️🔥 Zyada hi garami!")
    print("Suraj seedha khopdi pe baitha hai 🌞😵")
