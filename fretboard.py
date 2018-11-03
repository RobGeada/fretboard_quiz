import random
import os

notes = ["A","A#/Bb","B","C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab"]*3
string_starts = [None,7,2,10,5,0,7]
string_names  = [None,"E","B","G","D","A","E"]

def get_note(string,fret):
	return notes[string_starts[string]+fret]

dash  = "\033[30m-\033[0m"
block = "\033[90m█\033[0m"
fret_char = "\033[90m|\033[0m"
mark = "\033[1mⓍ\033[0m"

def disp_string(string):
	glyph = [None,dash,dash,block,block,dash,dash][string]

	out = [fret_char,dash,dash,dash]*22
	for i in [3,5,7,9,12,15,17,19,21]:
		if string in [2,5] and i==12:
			out[i*4-2]=block
		else:
			out[i*4-2]=glyph
	return [fret_char,string_names[string]]+out+[fret_char]

def quiz(note,guess):
	reg_note = note.lower()
	guess = guess.lower()

	if "/" in note:
		valid_answer = reg_note.split("/")
	else:
		valid_answer = [reg_note]

	if guess in valid_answer:
		print("\033[32mCorrect!\033[0m Note is {}".format(note))
	else:
		print("\033[31mIncorrect.\033[0m Note is {}".format(note))
	input("Hit enter to continue... ")

def fret_mode():
	while 1:
		fret   = random.randint(0,22)

		for string in [6,5,4,3,2,1]:
			os.system('clear')
			print("Fret mode")
			note = get_note(string,fret)

			print("\033[90m            3       5       7       9           12          15      17      19      21\033[0m")
			for j in range(1,7):
				out = disp_string(j)
				if j==string: 
					if fret==0:
						out[1]=mark
					else:
						out[2+fret*4-3]=mark
				print("".join(out))
			quiz(note,input("Note? "))

def random_mode():
	while 1:
		os.system('clear')
		print("Random mode")
		fret   = random.randint(0,22)
		string = random.randint(1,6)	
		note = get_note(string,fret)

		print("\033[90m            3       5       7       9           12          15      17      19      21\033[0m")
		for j in range(1,7):
			out = disp_string(j)
			if j==string: 
				if fret==0:
					out[1]=mark
				else:
					out[2+fret*4-3]=mark
			print("".join(out))
		quiz(note,input("Note? "))


if __name__ == '__main__':
	os.system('clear')
	print("=== FRETBOARD QUIZ ===")
	print("1) Random Mode")
	print("2) Fret Node")
	mode = input("Select Mode (1,2): ")

	if mode == '1':
		random_mode()
	else:
		fret_mode()

