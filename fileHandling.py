# IMPORTS-------------
from random import shuffle
import re


def writeToFile(question, options):

    fileText = question[0].strip()
    
    for each in options:
        fileText+= "\n" + each.strip()

    fileText += "\n\n\n"

    fout = open('new_formatted_file.txt', 'a')
    fout.write(fileText)


# Function to format the given input lines
def formatOutput(line):
    # Stripping the exccess whitespaces
    line = line.strip()

    endMarker = ":?"


    # Splitting the data based on ,
    data = line.split(",")
    actualLen = len(data)

     # This list represents the options for the question.`
    #  Splitting the question

    question =  data[0].split("(")
    # The holder for the answersppython
    options = list()

    # popping the extra option in the question 
    temp = question.pop(1)
    temp = "(" + temp
    options.append(temp)

    # Appending the options data in the options list
    for ind in range(1, actualLen):
        options.append(data[ind])

    # //Shuffling the options list
    shuffle(options)

    # Removing the predefined options
    finalOptions = list()
    asciiIndex = 97
    # traversing throught the list
    for each in options:
        temp = re.sub(r'\(.\)',"", each)

        temp = "(" + chr(asciiIndex) + ")" + temp.strip()
        finalOptions.append(temp)
        asciiIndex +=1



        # now assigning new values
    

    # Now for the other questions
    


    writeToFile(question, finalOptions)



# Handelling exception to open the file
try:
    # Openiing the file
    fhand = open('input_file.txt');

    # Reading all the data from the file
    data = fhand.read()
except:
    
    print("Error the file cannot be opened .")
    exit() # If file opening fails, then close the program


# //Splitting the file based on . new lines. 
# This returns a list of four data
questions = data.split(".\n")
del questions[len(questions) - 1]

# Traversing through each list question
for each in questions:
    formatOutput(each)
    





#  data = line.split(",")
