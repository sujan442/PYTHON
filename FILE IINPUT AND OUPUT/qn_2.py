import random

def game():
    print("You are playing a game...")
    score = random.randint(1, 100)
    print(f"Your score: {score}")

    try:
        with open("hello.txt", "r") as save:
            hi_score = save.read().strip()
            hi_score = int(hi_score) 
            if (hi_score!=0):
                hi_score=int(hi_score)
            else:
                return 1
    except FileNotFoundError:
        hi_score = 0

    if score > hi_score:
        with open("hello.txt", "w") as new:
            new.write(str(score))
        print("🎉 New high score!")
    else:
        print(f"High score remains: {hi_score}")

    return score

# Run the game
game()
