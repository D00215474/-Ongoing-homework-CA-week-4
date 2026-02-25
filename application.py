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

        try:
            # Split the line into parts using the "%%" delimiter and store the product information in a list. If the line does not contain the expected number of parts, catch the exception and print an error message.
            product_info.append(parts[1])
            product_info.append(parts[2])

            try: 
                product_info.append(float(parts[3]))
            except:
                print("Error: Cost price is not a valid number. Skipping line.")
                exit()
            
            try:
                product_info.append(int(parts[4]))
            except:
                print("Error: Quantity in stock is not a valid number. Skipping line.")
                exit()
            
            try:
                product_info.append(float(parts[5]))
            except:
                print("Error: Retail price is not a valid number. Skipping line.")
                exit()
            
            if parts[0] == "book":
                try:
                    product_info.append(parts[6])
                    genre_list = parts[7].split("%%")
                    product_info.append(genre_list)
                except:
                    print("Error: Book genre(s) is not in the expected format. Skipping line.")
                    exit()
                    
            display(product_info) # display the product details using the display function

        except IndexError:
            print("Error: Line does not contain the expected number of parts. Skipping line.")
            exit()
            
    print("End of file reached.")

