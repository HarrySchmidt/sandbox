"""Harry Schmidt"""
name = input("Input name: ")
while name == "":
    print("please input your name")
    name = input("Input name: ")
print(name[::2])