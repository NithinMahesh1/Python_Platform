from openpyxl import Workbook

def trainingSet():
    print("Connection successful")

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
    sheet = book.active

    count = 0
    val = input("Enter your a number for input values: ")

    if val == "q":
        exit()

    print("printing letters... " + val)

    for i in range(int(val)):
        count = count + 1
        sheet['A' + str(count)] = "G"

    book.save("test.xlsx")
    exit()


def testingSet():
    print("Connection Successful")

    val = input("Enter a number to generate random letters: ")
    print(val)

    if val == "q":
        exit()


def node():
    print("Connection Successful")