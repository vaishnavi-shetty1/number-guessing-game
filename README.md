# number-guessing-game
Welcome to the Number Guessing Game! This is a simple game where you try to guess a randomly generated number within a given number of attempts.

*Features:*
* The game selects a random number between 0 and 99.
* You have 7 attempts to guess the correct number.
* After each guess, the game gives you feedback:
  * If your guess is higher or lower than the target number.
  * If you guess the number correctly, the game congratulates you and tells you how many attempts it took.
  * If you run out of attempts without guessing the number, the game reveals the correct number.

Code Overview:

*The main components of the game are:*
* A randomly generated number between 0 and 99.
* A loop that runs 7 times (the number of allowed guesses).
* A check after each guess to see if it's too high, too low, or correct.
* If the correct number is guessed within the allowed attempts, the game congratulates the player; otherwise, it shows the correct number after 7 failed guesses.
