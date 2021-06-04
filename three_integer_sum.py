first_integer = int(input("Type your first integer: ")) 
second_integer = int(input("Type your second integer: "))
third_integer = int(input("Type your third integer: "))

total = first_integer + second_integer + third_integer

if(first_integer != second_integer and second_integer != third_integer and third_integer != first_integer):
    print(total)
else:
    print(0)
