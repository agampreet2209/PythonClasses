import os

# we will create program will create notes files for us

choice = int(input("What's your plan\n1. Read a note\n2. Write a note\n3. Append a Note\n4. Delete a Note\n\nEnter your choice : "))

note_title = input("\nEnter Note Title: ")

def readANote():
	try:
		noteFile = open(note_title, "r")
		print("\nOpening note...\n")
		print("--------Note Start--------")
		print(noteFile.read())
		print("--------Note End--------")
		noteFile.close()
	except:
		print("Erorr: Note Doesn't exist")


def createANote():
	try:
		noteFile = open(note_title, "x")
		print(f'{note_title} file created succesfully.')

		note = input("Please enter your notes : ")

		noteFile.write(note)
		

		print("Notes saved.")

		noteFile.close()
	except:
		print(f'{note_title} file already exist. Please choose another name')


def appendANote():
	try:
		readANote()
		noteFile = open(note_title, "a")
		note = input("Please enter your notes : ")
		noteFile.write(note)
		print("Notes saved.")
		noteFile.close()
	except:
		print("Error: Cannot append to note.")


def deleteANote():
	try:
		if os.path.exists(note_title):
			readANote()
			confirmation = input(f'\nAre you sure to Delete {note_title} (y/n) : ')
			if confirmation == "y":
				print("deleting...")
				os.remove(note_title)
				print("File deleted Succefully")
			else:
				print("cancelled")
		else:
		  	print("The file does not exist")
	except:
		print("Error in deleting note.")


if choice==1:
	readANote()
elif choice==2:
	createANote()
elif choice==3:
	appendANote()
elif choice==4:
	deleteANote()
