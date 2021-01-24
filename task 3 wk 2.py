'''
write a program which will ask user for two numbers, then offer menue to
the user (print option) giving them a choice of operators (a,f). Once the user
has seleceted which operator (input) they wish to use, perform the calculation using
a procedure and passing parameters.
'''
# Import math Library
import math

def procedure_add(int_numberOne, int_numberTwo):
     print("addition is " + str(int_numberOne + int_numberTwo))

def procedure_subtract(int_numberOne, int_numberTwo):
     print("subtraction is " + str(int_numberOne - int_numberTwo))

def procedure_divide(int_numberOne, int_numberTwo):
     print("divide is " + str(int_numberOne / int_numberTwo))

def procedure_multiply(int_numberOne, int_numberTwo):
     print("multiply is " + str(int_numberOne * int_numberTwo))

def procedure_powerof(int_numberOne, int_numberTwo):
     print("power of is " + str(math.pow(int_numberOne, int_numberTwo)))
     
     
#Accept 2 numbers via the user input
numberOne=int(input("Enter a First Number:"))
numberTwo=int(input("Enter a Second Number Two:"))


#Print menu to the user screen
print("enter 'a' if you want to add")
print("enter 'b' if you want to subtract")
print("enter 'c' if you want to divide")
print("enter 'd' if you want to multiply")
print("enter 'e' if you want to power of")
#Enter Operator option
operator=input("Please choose an operator: ")

if (operator=="a"):
     procedure_add(numberOne, numberTwo)
elif(operator=="b"):
     procedure_subtract(numberOne, numberTwo)
elif(operator=="c"):
    procedure_divide(numberOne, numberTwo)
elif(operator=="d"):
    procedure_multiply(numberOne, numberTwo)
elif(operator=="e"):
    procedure_powerof(numberOne, numberTwo)
else:
    print("you didnt choose an option")

 


