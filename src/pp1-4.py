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
# try:
#     num = int(input("Enter a number "))
# except ValueError:
#     print("Invalid input")
#     exit()
# l = range(1, num)
# print([i for i in l if num%i == 0])

# Ex 5
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print([x for x in a if x in b])

# Ex 6
# s = input("Enter a string ")
# i = len(s)//2
# print ("Palindrome" if s[0:i:1] == s[:i-1:-1] else "Not Palindrome")

# Ex 7
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print([x for x in a if x%2==0])

# Ex 8
# pl1 = input("Enter Rock(r) or Paper(p) or Scissors(s) for player 1: ");
# pl2 = input("Enter Rock(r) or Paper(p) or Scissors(s) for player 2: ");
# print("Player 1 won" if (pl1=="r" and pl2=="s") or (pl1=="s" and pl2=='p') or (pl1=='p' and pl2=='s') else "Player 2 won")

# Ex 9
# import random
# def getRandomNumber():
#     return random.randint(1,9)
#
# count = 0
# while True:
#     rand = getRandomNumber()
#     print("Random Number " + str(rand))
#     inpStr = input("Enter a number: ")
#     if (inpStr.lower()=="exit"):
#         break
#     else:
#         inp = int(inpStr)
#         print("Exact" if rand==inp else "Greater" if rand<inp else "Less")
#     count+=1
#
# print("Total Guesses: " + str(count))

# Ex 10
