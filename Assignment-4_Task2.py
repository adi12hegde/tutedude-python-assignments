#input("Enter text to write to the file: ")
with open ('output.txt','w') as file:
        file.write(input("Enter text to write to the file: "))
        print("Data successfully written to output.txt.")

with open ('output.txt','a') as file:
        file.write("\n"+input("\nEnter additional text to append: "))
        print("Data successfully appended")

with open ('output.txt','r') as file:
        print("\nFinal content of output.txt")
        for line in file.readlines():
                print(line)