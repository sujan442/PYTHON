import random
user=input("enter your choice:")
yourdict = {"s": "snake", "w": "water", "g": "gun"}
# yourdict={"s":1, "w":-1, "g":0}
# revdict={1:"snake",-1:"water",0:"gun"}
computer=random.choice(list(yourdict.keys())) #Writing list(yourdict.keys()) makes it explicit that you're choosing from the keys
# This converts the dictionary keys into a regular list:
# list(yourdict.keys())  →  ['s', 'w', 'g']

print("user choose:",user)# younum=yourdict[user]
print("computer choose:",computer)

if (computer==user):
    print("it's a draw:")

elif(user=="s"):
    if(computer=="w"):
        print("snake drinks water,You lose!")

    else:
        print("gun shoot snake,You win!")

elif(user=="w"):
    if(computer=="g"):
        print("water flew gun,You win!")

    else:
        print("snake drinks water,You lose!")

elif(user=="g"):
    if(computer=="s"):
        print("gun shoot snake,You win!")

    else:
        print("water flew gun, You lose!")

else:
    print("wrong")
