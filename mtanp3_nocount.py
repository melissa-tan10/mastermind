# Melissa Tan
# October 11, 2020
# This is a Mastermind game between a player and the computer

legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']


def generate_color_sequence():
    import random
    random.seed()

    sequence = random.sample(range(len(legal_colors)), 4)
    return [legal_colors[i] for i in sequence]

colors = generate_color_sequence()

### You Code Here


print("Possible colors are R, G, B, Y, W, O, M, V.")
print("Please enter your guess with no spaces between colors. Colors cannot be repeated.")

i = 1
while i <= 5:
     guess = input(f"\nGuess {i}:")
     guess = guess.upper()
     i += 1
     if len(guess) != 4:
          print("\nPlease enter 4 letters: ")
          i -= 1
     elif guess[0] == guess[1]:
          print("\nCannot repeat letters. Try again.")
          i -= 1
     elif guess[0] == guess[2]:
          print("\nCannot repeat letters. Try again.")
          i -= 1
     elif guess[0] == guess[3]:
          print("\nCannot repeat letters. Try again.")
          i -= 1
     elif guess[1] == guess[2]:
          print("\nCannot repeat letters. Try again.")
          i -= 1
     elif guess[1] == guess[3]:
          print("\nCannot repeat letters. Try again.")
          i -= 1
     elif guess[2] == guess[3]:
          print("\nCannot repeat letters. Try again.")
          i -= 1
     else:
          for index in range(len(guess)):
               if guess[index] == colors[index]:
                    print("R", end = '')
               elif guess[index] in colors:
                    print("W", end = '')
               elif guess[index] not in legal_colors:
                    print(f"\n{guess[index]} is not a valid color. Try again.")
                    i -= 1
               else:
                    guess[index] not in colors
                    print("_", end = '')
     guess = list(guess)
     if guess == colors:
          print("\nYou win!")
          quit()
     if i > 5:
          print("\nYou lose!")


















