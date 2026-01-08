def main():
    # ask the user how many numbers they would like to enter
    # loop to get that many numbers from the user
    # validate that the input is a number
    # store the numbers in a list
    # print the list of numbers

    numbers = []

    count = int(input("How many numbers would you like to enter?: "))
    while True:
        if count > 0:
            break
        try:
            count = int(input("Please enter a positive integer for how many numbers you'd like to enter: "))
            if count <= 0:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    print("You entered the following numbers:")
    for num in numbers:
        print(num, end=" ")
        print()



    


if __name__ == "__main__":
    main()

