def display(data):
    print("Product details:")
    print(f"\tID: {data[0]}")
    print(f"\tName: {data[1]}")
    if len(data) == 7:
        print(f"\tAuthor: {data[5]}")
    print(f"\tCost price: {data[2]}")
    print(f"\tRetail price: {data[3]}")
    print(f"\tQuantity in stock: {data[4]}")
    if len(data) == 7:
        print(f"\tGenre(s): {data[6]}")

filename = input("Please enter the inventory filename: ")

# Initialize the number of tries and the total number of tries allowed.
trys = 0
total_tries = 5

# Try to open the file and read the first line. If the file is not found, catch the exception and increment the number of tries. Calculate the number of tries left and print an error message. If there are no tries left, exit the program..
while trys < total_tries:
    filename = input("Please enter the inventory filename: ")

    try:
        #try to open the file and read the first line
        with open(filename, "r") as file:
            print("File opened successfully.")
            break

# if the file is not found, catch the exception and increment the number of tries. Calculate the number of tries left and print an error message. If there are no tries left, exit the program.
    except FileNotFoundError:
        trys = trys + 1
        trys_left = total_tries - trys

# if the file is not found, print an error message and the number of tries left. If there are no tries left, exit the program.
        if trys_left > 0:
            print("File not found. Please try again.")
            print("you have", trys_left, "tries left.")
        else:
            print("File not found. No more tries left. Exiting program.")
            exit()

# If the file is opened successfully, read the file line by line and display the product details. Skip empty lines.
while file:
    for line in file:
        line = line.strip()
        if line == "": #skip empty lines
            continue

# Split the line into parts using the "%%" delimiter and store the product information in a list. If the line does not contain the expected number of parts, catch the exception and print an error message.
        parts = line.split("%%")
        product_info = []



