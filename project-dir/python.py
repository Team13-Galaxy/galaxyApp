import os

# Define the directory and file names
directory_name = "my_new_directory"
file_name = "my_new_file.txt"

# Create the directory
try:
    os.makedirs(directory_name, exist_ok=True)
    print(f"Directory '{directory_name}' created successfully (or already exists).")
except OSError as e:
    print(f"Error creating directory '{directory_name}': {e}")

# Create the file inside the directory
file_path = os.path.join(directory_name, file_name)
try:
    with open(file_path, 'w') as f:
        f.write("This is some content for the new file.")
    print(f"File '{file_name}' created successfully in '{directory_name}'.")
except IOError as e:
    print(f"Error creating file '{file_name}': {e}")