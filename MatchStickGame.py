import random as r
import time

print("Welcome to Match Stick Game...")
n = input("\nYour Name:\n")
n = n.upper()
print()
print("Players to choose at least 1 to 5 match stick(s)...")
print("Please choose between 1 to 5 !")
print("Player whose at least 1 match stick left is the looser...")
t = 21
while t != 1:
    print(n, "Please Choose:")
    c = int(input())
    if c < 1:
        print("Please choose between 1 to 5 !")
    elif c > 5:
        print("Please choose between 1 to 5 !")
    elif (t - c) == 0:
        print(n, "Has Exhausted All the Matchsticks ...")
        print("\nCOMPUTER WINS!!!")
        break
    elif (t - c) < 1:
        print("Choose Correctly!")
    else:
        t -= c
        print("     TOTAL NUMBER OF MATCH STICKS =", t)
        print("_" * t + "\n" + "|" * t)
        if t > 6:
            c1 = r.randint(1, 5)
        elif t >= 2:
            c1 = t - 1
        else:
            print("Congratulations !!!")
            print(n, "WINS ...")
            break
        print("Computer:""\n", c1)
        t -= c1
        print("     TOTAL NUMBER OF MATCH STICKS =", t)
        print("_" * t + "\n" + "|" * t)
        if t == 1:
            print("COMPUTER WINS!!!")

for i in range(10):
    print("Program khatam ho gya hai window close karlo")
    time.sleep(3)