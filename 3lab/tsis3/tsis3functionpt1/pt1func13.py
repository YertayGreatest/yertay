import random

    
randomnum = random.randint(1,20)

    
name = input(print("Hello! What is your name? "))


def guessing(attempt):
    take = int(input("Take a guess: "))
    if take==randomnum:
        print(take,"Good job, ",name,"! You guessed my number in ",attempt+1," guesses!")
    elif take>randomnum:
        print(take,"Your guess is higher")
        attempt+=1
        guessing(attempt)
    else:
        print(take,"Your guess is too low")
        attempt+=1
        guessing(attempt)
print("Well",name,", I am thinking of a number between 1 and 20")
first = input("Take a guess: ")
guessing(attempt=1)


    
          
