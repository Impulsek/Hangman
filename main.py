import math
import random
import os

def main():
	game=input("Do you want to play hangman? Y=yes N=no: ")
	while(game=="y"):
		#reading words from file
		words=open("words.txt","r")
		bank=["word"]
		if words.mode == "r":
			contents = words.read().splitlines()
		attempts=11 #5 to stand and 6 as human
		#randomizing word from array and creating word template to show to player
		rnd=random.randint(0,9897) #9898 words
		word=contents[rnd]
		wordlen=len(word)
		guess=[]
		letters=[]
		for character in word:
			guess.append("-")
		guessrpl=0 #0 for first round, after that 1-correct, 2-incorrect
		attempt="" #variable with input character
		while attempts>0:
			while True:
				os.system('cls')
				if guessrpl == 1:
					print("You guessed correctly!\n")
				elif guessrpl == 2:
					print('You did not guessed right :< Try again!\n')
				elif guessrpl == 3:
					print('You choose already this letter! Try another one.')
				print("Guess the word! You have",attempts,"attempts left\n")
				print("\nLetters already used: ", letters,"\n")
				print("Word to guess:")
				print (guess)
				attempt=input("\nYour type:")
				if attempt not in letters:
					letters.append(attempt)
					break
				else:
					guessrpl = 3
			if attempt in word:
				guessrpl=1
				for x in range (0, wordlen):
					if word[x]==attempt:
						guess[x]=attempt #insert guess letter to storage to print
				if not '-' in guess:
					break
			else:
				guessrpl=2
				attempts=attempts-1
		if attempts==0:
			game=input("You lost! Do you want to try again? Y=yes N=no: ")
			if(game!="y"):
				print("Bye bye! :)")
				break
		else:
			game=input("You won! Do you want to try again? Y=yes N=no: ")
			if(game!="y"):
				print("Bye bye! :)")
				break
if __name__=="__main__":
	main()