#TASK: Read something from the a text file, and output it on another text file

#open the file
fileInput = open("put the file directory here", "r")

#print("The contents of the file is: ")
print("The contents will be read here!")
#read and print the file; all of its contents
fileOut = fileInput.read()
#print(fileOut)

print("")
print("")
print("")
print("Currenty moving ...")
print("")
print("")
print("")
print("Processing ...")
print("")
print("")
print("")

print ("The contents are now moved!")
#write the output of fileInput to another file
fileOutput = open("put the file directory here", "w")
fileOutHere = fileOutput.write(fileOut)

#close the file
fileInput.close()
fileOutput.close()
