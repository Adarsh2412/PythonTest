#function calculator is defined
def calculator(first_number,second_number,operation):
    if(operation=='add'):#if input is add, then we will add the numbers
        return first_number+second_number
    elif(operation=='subtract'):#if input is subtract, then we will subtract the numbers
        return first_number-second_number
    else:#if input is not add or subtract, then error should be returned
        return "error"
first=(int)(input("Enter first number: "))
second=(int)(input("Enter second number: "))
symbol=input("Enter the operation-add or subtract: ")
answer=calculator(first,second,symbol)
if(answer=="error"):#if returned value is 'error' then that means, wrong symbol input
    print("Please check the operation entered, as there seems to be invalid input, the symbol you entered is "+symbol+" ,it should be add or subtract")
else:
    print("Answer is "+str(answer))
