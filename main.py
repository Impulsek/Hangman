import random
import os

menu = ""
attempts = 11
attempt = ""
guessrpl = 0
word = ""
wordlen = 0

def file():
	global wordlen
	global word

	words=open("words.txt","r")
	bank=["word"]
	if words.mode == "r":
		contents = words.read().splitlines()
	rnd=random.randint(0,9897) #9898 words
	word=contents[rnd]
	wordlen=len(word)

def game():
	global attempts
	global attempt
	global guessrpl
	global word
	global wordlen
	
	attempts = 11
	guessrpl = 0
	guess=[]
	letters=[]
	words=[]
	file()
	for character in word:
			guess.append("-")
	while attempts>0:
		while True:
			os.system('cls')
			if guessrpl == 1:
				print("You guessed correctly!\n")
			elif guessrpl == 2:
				print("You didn't guess right :< Try again!\n")
			elif guessrpl == 3:
				print('You already tried this letter! Try another one.\n')
			elif guessrpl == 4:
				print('You already tried this word! Try another one.\n')
			print("Guess the word! You have",attempts,"attempts left\n")
			print("\nLetters already used: ", letters,"\n")
			print("\nWords tried: ",words,"\n")
			print("Word to guess:")
			print(guess)
			print(word)
			attempt=input("\nYour type: ")
			if len(attempt)<2:
				if attempt not in letters:
					letters.append(attempt)
					break
				else:
					guessrpl = 3
			else:
				if attempt not in words:
					words.append(attempt)
					break
				else:
					guessrpl = 4
		if len(attempt)>1:
			if attempt == word:
				end()
			else:
				attempts=attempts-1
				guessrpl = 2
		elif attempt in word:
			
			guessrpl=1
			for x in range (0, wordlen):
				if word[x]==attempt:
					guess[x]=attempt #insert guess letter to storage to print
			if not '-' in guess:
				end()
		else:
			guessrpl=2
			attempts=attempts-1
	

def end():
	global menu
	global attempts

	if menu == "n":
		print("Bye bye :)")
		exit()
		
	if attempts < 1:
		os.system('cls')
		while True:
			menu=input("You lost! Do you want to try again? Y=yes N=no: ")
			if(menu == "n"):
				print("Bye bye! :)")
				exit()
			elif menu == "y":
				attempts = 11
				game()
				
	elif attempts>0:
		os.system('cls')
		while True:
			menu = input("You won! Do you want to try again? Y=yes N=no: ")
			if(menu == "n"):
				print("Bye bye! :)")
				exit()
			elif menu == "y":
				attempts = 11
				game()
				
def start():
	global menu
	startvar = 1
	
	while startvar == 1:
		os.system('cls')
		menu = input('Do you want to play hangman? Y=yes N=no: ')
		if menu == "y":
			startvar = 0
			game()
		elif menu == "n":
			end()
			
if __name__ == "__main__":
	start()