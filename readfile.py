file1 = open("myfile.txt","w")
L = ["My name is venkatesh./n How can I help you?"]
file1.writelines(L)
file1 = open("myfile.txt", "r+")

print(file1.read())
