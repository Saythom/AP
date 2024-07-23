
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":
    width =num_check("width= ")
    height =num_check("height= ")
    cost =num_check("cost per/m= ")

    # Calculate perimeter and price for the fence
    perimeter = (width + height) * 2
    price = perimeter * cost

    # display output
    print()
    print(f"perimeter: {perimeter} units")
    print(f"price: ${price:.2f}")

   #ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()
    print()

print("Thank you for using the fence cost calculator")
