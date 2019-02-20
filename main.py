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
		for character in word:
			guess.append("-")
		while attempts>0:
			os.system('cls')
			print("Guess the word! You have",attempts,"attempts left\n")
			print (guess)
			attempt=input("\nYour type:")
			if attempt in word:
				print("You guessed correctly!\n")
				for x in range (0, wordlen):
					if word[x]==attempt:
						guess[x]=attempt #insert guess letter to storage to print
				if not '-' in guess:
					break
			else:
				print('You did not guessed right :< Try again!\n')
				attempts=attempts-1
		if attempts==0:
			game=input("You lost! Do you want to try again? Y=yes N=no: ")
			if(game!="y"):
				break
		else:
			game=input("You won! Do you want to try again? Y=yes N=no: ")
			if(game!="y"):
				break
if __name__=="__main__":
	main()