# Read the contents of example_file.txt
example_file = open("example_file.txt", "r")
file_contents = example_file.read()
example_file.close()
print(file_contents)

# Write to new_file.txt
new_file = open("new_file.txt", "w")
new_file.write("This is a new file with some content.\n")
new_file.close()

# Read and print the contents of new_file.txt
new_file = open("new_file.txt", "r")
new_file_contents = new_file.read()
new_file.close()
print(new_file_contents)

# Append to new_file.txt
append_file = open("new_file.txt", "a")
append_file.write("Appending new content.\n")
append_file.close()

# Read and print each line of new_file.txt
line_file = open("new_file.txt", "r")
for line in line_file:
    print(line, end="")
line_file.close()
