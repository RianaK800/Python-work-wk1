#Accept 2 numbers via the user inout
numberOne=int(input("Enter a First Number:"))
numberTwo=int(input("Enter a Second Number Two:"))


#Print menu to the user screen
print("enter 'a' if you want to add")
print("enter 'b' if you want to subtract")
print("enter 'c' if you want to divide")
print("enter 'd' if you want to multiply")
print("enter 'e' if you want to power of")
print("enter 'f' if you want to square of")
#Enter Operator option
operator=input("Please choose an operator: ")

if (operator=="a"):
     print("addition is " + str(numberOne + numberTwo))
elif(operator=="b"):
     print("subtraction is " + str(numberOne - numberTwo))
elif(operator=="c"):
    print("division is " + str(numberOne / numberTwo))
elif(operator=="d"):
    print("multiplication is " + str(numberOne * numberTwo))
elif(operator=="e"):
    print("power of is " + str(math.power(numberOne, numberTwo)))
else:
    print("you didnt choose an option")

 
