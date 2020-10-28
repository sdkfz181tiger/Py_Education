# coding: utf-8

# Comment
print("Hello World!!")

FILE_NAME = "test.txt"

text = "Hello, how are you?"
file = open(FILE_NAME, "w")
file.write(text)
file.close();