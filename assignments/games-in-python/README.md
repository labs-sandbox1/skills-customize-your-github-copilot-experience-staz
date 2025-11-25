

# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python. Practice string manipulation, loops, conditionals, and random selection by creating a word-guessing game where players try to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Hangman Game Logic

#### Description
Create the main game loop for Hangman. The program should randomly select a word, accept letter guesses, and display the current progress. Track incorrect guesses and end the game with a win or lose message.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept letter guesses from the user
- Show current progress using underscores for unguessed letters (e.g., _ a _ _ m a n)
- Track and display the number of incorrect guesses remaining
- End when the word is fully guessed or attempts are exhausted
- Display a win message if the player guesses the word, or a lose message if they run out of attempts

### 🛠️ User Experience & Input Validation

#### Description
Improve the user experience by validating input and providing clear instructions and feedback.

#### Requirements
Completed program should:

- Prompt the user with clear instructions at the start
- Validate that guesses are single alphabetic characters
- Prevent repeated guesses and notify the user
- Show guessed letters and incorrect guesses so far
- Handle both uppercase and lowercase input consistently
