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
        
trys = 0
total_tries = 5

while trys < total_tries:
    filename = input("Please enter the inventory filename: ")

    try:
        file_handle = open(filename, "r")
        print("File opened successfully.")
        break # Exit the loop if the file is opened successfully

    except FileNotFoundError:
        

