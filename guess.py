import random
print("HI!! \nWelcome to the game.\n You got 7 chances to guess the number.\n Let's start the game.")

number_to_guess=random.randrange(100)

chances=7

guess_counter=0

while guess_counter < chances:
  guess_counter+=1
  myguess=int(input('Please Enter your Guess:'))

  if myguess == number_to_guess:
    print(f'The number is {number_to_guess} and you found it right in {guess_counter}
 attemp!!')
    break
 
elif guess_counter >= chances and myguess != number_to_guess:
  print(f' Sorry !! The number is {number_to_guess} better luck next time')

elif myguess > number_to_guess:
  print('Your guess is higher')

elif myguess < number_to_guess:
  print('Your guess is lower')

