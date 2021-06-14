import os 



choice = int(input("You need help in which thing\n. Reading a note\n. Writing a note\n. Apend a note\n. delete a note\n\nEnter you choice : "))

note_title = input("Enter Note Title: ")

def readinganote():
	try:
		notefile = open(note_title, "r")
		print("\nnote opening....\n")
		print("------Note Start-------")
		print(notefile.read())
		print("------Note End-------")
		notefile.close()
	except:
		print("error: Note does not exhist")


def writinganote():
	try:
		notefile = open(note_title, "x")
		print(f'{note_title} file created succesfully.')

		note = input("please enter your note: ")

		notefile.write(note)

		print("notes created and saved succesfully.")

		notefile.close()

	except:
		print(f'{note_title} file already exist. Please choose another name')

 
def apendanote():
	try:
		readinganote()
		notefile = open(note_title, "a")
		note = input("please enter your notes : ")
		notefile.write(note)
		print("Notes saved.")
		notefile.close()
	except:
		print("Error: Cannot append to note.")



if choice==1:
	readinganote()
if choice==2:
	writinganote()		
if choice==3:
	apendanote()		