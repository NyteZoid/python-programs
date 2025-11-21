#start

import random

words = ["APPLE","BRAIN","CHAIR","PLANT","STARS","HOUSE","MUSIC","LIGHT","SUGAR","POWER",
         "SWEET","TABLE","WATCH","RIVER","NIGHT","FIGHT","SIGHT","KNIFE","STAMP","GRAPE",
         "CLOUD","DANCE","SPACE","SPEED","BREAD","PHONE","FRUIT","IMAGE","PIZZA","TOAST",
         "TRAIN","DRIVE","HORSE","MONEY"]

secret = random.choice(words)

print("WELCOME TO WORDLE! 🎯")
print("Guess the 5 letter word. You have 6 attempts")

for x in range(6):
    guess = input(f"Attempt {x+1}/6: ").upper()

    if len(guess) != 5 or guess.isalpha() == False:
        print("⚠️ Please enter a valid 5 letter word")
        continue

    feedback = []
    for n in range(5):
        if guess[n] == secret[n]:
            feedback.append("🟩")
        elif guess[n] in secret:
            feedback.append("🟨")
        else:
            feedback.append("🟥")

    print(" ".join(feedback))

    if guess == secret:
        print(f"🎉 Congrats! You guessed it in {x+1} tries")
        break

else:
    print(f"❌ Out of tries! The word was {secret}")

#end
