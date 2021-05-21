# lets start
myIntroFile = open("agam_way.txt", "a")
msg = input("Type your Introduction here : ")

myIntroFile.write(msg)

# after your work completed always close a file
myIntroFile.close()