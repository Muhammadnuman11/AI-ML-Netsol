
age = 20
if age>= 18:
    print("You are an adult")

if age>= 18:
    print("Adult")
else:
    print("Minor")


number = 7

if number % 2 == 0:
    print("Evan")
else:
    print("Odd")


marks = 75

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 40:
    grade = "E"
else:
    grade = "F"
print(grade)


age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")

x = int(input("Enter No."))
result = "A" if x > 90 else "B" if x>80 else "C" if x > 70 else "D"
print(result)