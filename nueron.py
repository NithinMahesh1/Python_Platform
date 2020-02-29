from openpyxl import Workbook
import random
import xlrd

def trainingSet():
    # TODO Creating data set
    #     1. Data set will be a list of numbers either 0 or 1:
    #     Example 1:
    #           input: 0 1 1       output: 0
    #           input: 1 0 0       output: 1
    #           input: 0 0 0       output: 1

    # TODO Creating the nueral node class
    #    2. Write a nueral class object
    #       - Weights increase: Wx + b > 0 -> 1
    #                           Wx + b < 0 -> 0
    #       - Start with the same wieght of type double either from 0-1 maybe 0.5
    #       -

    # TODO Write a method to print out letters to excel sheet to create
    # training set data in which we give it the expected output
    # written in two programs one will be the student and the other will
    # be the teacher.

    book = Workbook()
    trainingSheet = book.active

    count = 0
    val = input("Enter your a number for input values: ")

    if val == "q":
        exit()

    print("printing letters... " + val)

    for i in range(int(val)):
        count = count + 1
        trainingSheet['A' + str(count)] = "G"
        trainingSheet['B' + str(count)] = 'Y'

    book.save("trainingSet.xlsx")
    exit()


def testingSet():
    book = Workbook()
    testingSheet = book.active
    count = 0

    val = input("Enter a number to generate random letters: ")

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if val == "q":
        exit()

    for i in range(int(val)):
        count = count + 1
        ramdomLetter = str(random.choice(letters))
        testingSheet['B' + str(count)] = 'N'
        if ramdomLetter == 'G':
            testingSheet['B' + str(count)] = 'Y'
        testingSheet['A' + str(count)] = ramdomLetter

    workbook = xlrd.open_workbook('testingSet.xlsx')


    book.save("testingSet.xlsx")
    exit()

def expectedResults():
    # TODO this is where we will create an expected output for training set
    # TODO also create another training set to give random letters but also if its a G give output of yes

    book = Workbook()


def node():
    print("Connection Successful")
