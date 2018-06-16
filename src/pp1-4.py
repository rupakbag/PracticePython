# Ex 1
# from datetime import date
# name = input("What is yr name ")
# age = input("Enter age ")
#
# date = date.today()
# print(name + " you will be 100 years old in " + str(int(date.year) + 100 - int(age)))


# Ex 2
# num = input("Enter a number ")
# print("The number you entered is " + "even" if int(num) % 2 == 0 else "odd")

# Ex 3
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print([x for x in a if x < 5])

# Ex 4
try:
    num = int(input("Enter a number "))
except ValueError:
    print("Invalid input")
    exit()
l = range(1, num)
print([i for i in l if num%i == 0])
