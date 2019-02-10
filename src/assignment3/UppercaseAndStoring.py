fileReader = open("resource.txt", "r")
words = "\n" + fileReader.read()

fileWriter = open("resource.txt", "a")
fileWriter.write(words.upper())

