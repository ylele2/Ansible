import os

# Define the file name and path
file_name = "example.txt"
file_path = "/tmp/" + file_name

# Create the file
with open(file_path, "w") as file:
    file.write("This is an example file created by Python!")

# Check if the file was created successfully
if os.path.exists(file_path):
    print("File created successfully at: " + file_path)
else:
    print("Failed to create file at: " + file_path)
