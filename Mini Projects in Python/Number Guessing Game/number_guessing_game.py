import random, math

print("Welcome to Guess the number :)")

# Taking lower and upper bounds from the user
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

# Generating a random number from the given range
number = random.randint(lower, upper)

# Calculating the number of chances by using the formula log2(upper - lower + 1)
chances = math.ceil(math.log(upper - lower + 1, 2))

print(f"You have total {chances} chances.")

while chances > 0:
    guess = int(input("Guess a number: "))
    
    if guess == number:
        print("Congratulations! You won.")
        break
    elif guess > number:
        print("Guess is higher than the number.")
        chances -= 1
        print(f"You have {chances} chances left.")
    else:
        print("Guess is lower than the number.")
        chances -= 1
        print(f"You have {chances} chances left.")
    
    

    if chances == 0:
        print(f"You have lost. The correct number was {number}. Better luck next time.")
