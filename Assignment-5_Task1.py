marks={'Alice':85,'Sara':97,'Mike':76,'Kelly':89}
name=input("Enter the student's name: ")
try:
    print(name+"'s Marks:",marks[name])
except KeyError:
    print("Student not found.")