#import the functions of the operators from the seperate file created
from functions import *

#ask the user what operation they want to carryout
#the 'while' is a loop that enables the function to be able to keep on running
while True:
    print(' Hello, which operation do you want to carryout? Choose from the options below.')
    print('     1 ADD')
    print('     2 SUBTRACT')
    print('     3 MULTIPLY')
    print('     4 DIVIDE')
    print('Type tired to exit ')

#the user must make a choice on the operation to be done
    choice = input('Please choose an operation to carryout ')

#the code that breaks the program
    if choice == 'tired':
        break

#prompt the user to enter the digits the operation should work on in number form
    num1 = float(input('Input first digit '))
    num2 = float(input('Input second digit '))

#set out and give each operation a method to work on
    if choice == '1':
        addition(num1, num2)

    elif choice == '2':
        subtraction(num1, num2)

    elif choice == '3':
        multiplication(num1, num2)

    elif choice == '4':
        division(num1, num2)

    else:
        print('Oops! Check the value entered and try again.')

#to put a space after all the results are displayed
    print('\n')
