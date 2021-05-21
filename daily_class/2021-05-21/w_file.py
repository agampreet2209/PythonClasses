# file handling deals with files e.g.: Image file, text file, video file, pdf file etc i.e any type of file
# so how it works?
# to Access a file you need to open it first 
# to do so we have a function 'open(param1, param2)' with 2 param
# param 1 -> name of file / file name with relative/absolute location
# param 2 -> access node of file
# Types of access mode -> r, a, w, x, t, b

# lets start
myIntroFile = open("agam_way.txt", "w")
msg = input("Type your Introduction here : ")

myIntroFile.write(msg)

# after your work completed always close a file
myIntroFile.close()


