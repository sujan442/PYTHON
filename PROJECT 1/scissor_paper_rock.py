import random
option=["scissor","paper","rock"]
computer=random.choice(option)
# user=user.lower()
user = input("Type either scissor, paper, or rock: ").lower()
# user=print("type either scissor paper or rock: ").lower()

print("Computer choose:",computer)


if (user==computer):
    print("It's a draw:")

elif user=="scissor":
     if computer=="rock":
          print("rock smashes scissor,You lose!")

     else:
        print("scissor cuts paper,You win!")

elif user=="paper":
    if computer=="scissor":
        print("scissor cuts paper,You lose!")

    else:
        print("paper smashes rock, You win!")

elif user=="rock":
    if computer=="paper":
        print("paper covers rock,You lose!")

    else:
        print("rock smashes scissor,You win!")

else:
    print("wrong input!")
