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

try:
    with open(filename, "r") as file_handle:
        # Read content of file in and store in a list of content
        for line in file_handle:
            line = line.strip()
            if not line:
                continue

            components = line.split("%%")
            data = []

            try:
                data.append(components[1])
                data.append(components[2])
                data.append(float(components[3]))
                data.append(float(components[4]))
                data.append(int(components[5]))
                if components[0] == "Book":
                    data.append(components[6])
                    genres = components[7].split("&&")
                    data.append(genres)

            except (IndexError, ValueError) as e:
                print("File Not Found")
                exit()

