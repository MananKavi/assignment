# Program to read from file and convert text into uppercase and again store it into file.
fileReader = open("resource.txt", "r")
words = "\n" + fileReader.read()

fileWriter = open("resource.txt", "a")
fileWriter.write(words.upper())

