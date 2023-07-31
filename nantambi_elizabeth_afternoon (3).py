#Exception Handling

try:
    file_path = input("Enter the file path: ")
    file = open(file_path, 'r') 
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied to access the file.")
except OSError as e:
    print("An OS error occurred:", str(e))
except Exception as e:
    print("Caught an exception:", str(e))
finally:
    print("Finally block executed")

print("\n")
print("================================================")



file_path = "liz.txt"

# Opening the file in read mode
file = open(file_path, 'r')

# Reading the contents of the file
content = file.read()
print(content)

# Closing the file
file.close()

file_path = "liz.txt"

# Open the file in write mode
file = open(file_path, 'w')

# Write content to the file using write() method
file.write("My name\n")
file.write(" is Nantambi.\n")
file.write("Elizabeth\n")

# Close the file
file.close()

# Open the file in read mode
file = open(file_path, 'r')

# Read the entire content 
content = file.read()
print("Content of the file:")
print(content)

# Close the file
file.close()

# Open the file in read mode
file = open(file_path, 'r')

# Read the file line by line 
print("Content of the file line by line:")
line = file.readline()
while line:
    print(line.strip())  
    line = file.readline()

# Close the file
file.close()

# Open the file in read mode
file = open(file_path, 'r')

# Read lines of the file
lines = file.readlines()
print("Content of the file using readlines():")
for line in lines:
    print(line.strip())

# Close the file
file.close()
