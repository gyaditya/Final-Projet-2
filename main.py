import random

class Hangman:
    def __init__(self, words):
        self.words = words
        self.word = random.choice(self.words).lower()
        self.guessedLetters = []
        self.incorrectGuesses = 0
        self.maxIncorrectGuesses = 6
        self.gameOver = False

    def play(self):
        while not self.gameOver:
            self.displayWord()
            self.getGuess()

    def displayWord(self):
        for i in range(len(self.word)):
            if self.word[i] in self.guessedLetters:
                print(self.word[i], end=" ")
            else:
                print("_", end=" ")
        print()

    def getGuess(self):
        if self.checkWin():
            print("You win!")
            self.gameOver = True
            return
        guess = input("Guess a letter: ").lower()
        if len(guess) > 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in self.guessedLetters:
            print("You already guessed that letter. Try again.")
        else:
            self.guessedLetters.append(guess)
            if guess in self.word:
                print("Correct.")
                if self.checkWin():
                    print("You win!")
                    self.gameOver = True
            else:
                self.incorrectGuesses += 1
                print("Incorrect.")
                remainingGuesses = self.maxIncorrectGuesses - self.incorrectGuesses
                if remainingGuesses == 0:
                    print("You lose! The word was " + self.word)
                    self.gameOver = True
                else:
                    print(f"You have {remainingGuesses} guesses left.")

    def checkWin(self):
        for i in range(len(self.word)):
            if self.word[i] not in self.guessedLetters:
                return False    
        return True




words = ["Ripped", "Jacked", "Money", "Dough", "Life"]

game = Hangman(words)
game.play()