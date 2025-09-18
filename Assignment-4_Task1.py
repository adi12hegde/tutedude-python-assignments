try:
    with open ('sample.txt','r') as file:
        print("Reading file content:")
        for line in file.readlines():
            print(line)
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
