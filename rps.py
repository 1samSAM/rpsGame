import random
useW = 0
dr=0
comW =0 

op = ["r","p","s"]

while True:
    print("\nEnter rock = r, paper = p ,scissor = s or quit = q")
    useI = input().lower()

    if useI == "q":
        break
    if useI not in op:
        continue
    
    randomN = random.randint(0,2)
    comI = op[randomN]

    if useI == comI:
        print("compter= ",comI)
        print("same")
        dr = 1 + dr
    elif useI=="r" and comI == "s":
        print("compter= ",comI)
        print("you win")
        useW += 1
    elif useI == "p" and comI == "r":
        print("compter= ",comI)
        print("You won!")
        useW += 1

    elif useI == "scissors" and comI == "paper":
        print("compter= ",comI)
        print("You won!")
        useW += 1

    else:
        print("compter= ",comI)
        print("You lost!")
        comW += 1

print("You won", useW, "times.")
print("The computer won", comW, "times.")
print("Goodbye!")
