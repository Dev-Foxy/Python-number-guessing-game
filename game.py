import random #for generating random number

guess_range = int(input("Enter range for the guess: "))

number = random.randint(0,guess_range) #generating random number between given range

guess = int(input("Enter a no to guess: "))

count = 0 #for counting try

while guess != number:
    if guess> number:
        print("Too high")
        count = count +1
        guess = int(input("Enter a no to guess: "))
    elif guess<number:
        print("Too low")
        count = count +1
        guess = int(input("Enter a no to guess: "))
    else:
        break

print("You got it after "+str(count)+" try")