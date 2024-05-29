# Open the file in read mode
example_file = open("example_file.txt", "r")

# Read the contents of the file
file_contents = example_file.read()

# Close the file
example_file.close()

# Print the contents of the file
print(file_contents)

# Open a new file in write mode
new_file = open("new_file.txt", "w")

# Write some content to the new file
new_file.write("This is a new file with some content.\n")

# Close the new file
new_file.close()

# Open the new file in read mode to verify its content
new_file = open("new_file.txt", "r")
new_file_contents = new_file.read()
new_file.close()

# Print the contents of the new file
print(new_file_contents)
