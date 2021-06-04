first_input_number = float(input("Please type your first number here: "))
second_input_number = float(input("Please type your second number here: "))

if(first_input_number > second_input_number):
    print("The larger number is: " + str(first_input_number))
elif(second_input_number > first_input_number):
    print("The larger number is: " + str(second_input_number))
elif(first_input_number == second_input_number or second_input_number == first_input_number):
    print("Both numbers are equal!")
elif(first_input_number == None):
    print("Please type the appropriate number convention.")
else:
    print("Please type the appropriate number convention.")

    