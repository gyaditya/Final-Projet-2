import random

class Hangman:
    def __init__(self):
        self.words = ["python", "programming", "computer", "science", "coding"]
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6

    def play(self):
        while True:
            self.display_word()
            self.get_guess()
            if self.check_win():
                print("You win!")
                break
            if self.check_lose():
                print("You lose! The word was " + self.word)
                break

    def display_word(self):
        for letter in self.word:
            if letter in self.guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()

    def get_guess(self):
        guess = input("Guess a letter: ").lower()
        if guess in self.guessed_letters:
            print("You already guessed that letter. Try again.")
            self.get_guess()
        elif len(guess) > 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            self.get_guess()
        else:
            self.guessed_letters.append(guess)
            if guess not in self.word:
                self.incorrect_guesses += 1
                print("Incorrect.")
                remaining_guesses = self.max_incorrect_guesses - self.incorrect_guesses
                print(f"You have {remaining_guesses} guesses left.")
            else:
                print("Correct.")

    def check_win(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def check_lose(self):
        return self.incorrect_guesses >= self.max_incorrect_guesses

game = Hangman()
game.play()
