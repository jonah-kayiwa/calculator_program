#set out the method for the addition operation
def addition(num1, num2):
    result = num1 + num2
#Take note that the 0,1 and 2 are just place holders for the digits to be input
    print('{0} + {1} = {2} '.format(num1, num2, result))

#set out the method for the subtraction operation
def subtraction(num1, num2):
    result = num1 - num2
#Take note that the 0,1 and 2 are just place holders for the digits to be input
    print('{0} - {1} = {2} '.format(num1, num2, result))    

#set out the method for the multiplication operation
def multiplication(num1, num2):
        result = num1 * num2
#Take note that the 0,1 and 2 are just place holders for the digits to be input
        print('{0} * {1} = {2} '.format(num1, num2, result))        

#set out the method for the division operation
def division(num1, num2):
#we shall not allow the program to divide by zero
            if num2 == 0.0:
                print("Bro, we don't do that here!")   
            else:             
                result = num1 / num2
#Take note that the 0,1 and 2 are just place holders for the digits to be input
            print('{0} / {1} = {2} '.format(num1, num2, result)) 