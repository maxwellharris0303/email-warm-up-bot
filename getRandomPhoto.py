import os
import random

def get_file_names(directory):
    file_names = []
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):
            file_names.append(file_name)
    return file_names

def generate_random_integer(count):
    random_integer = random.randint(0, count - 1)
    return random_integer

# Specify the directory path
directory_path = 'photo'

# Get the file names in the directory
files = get_file_names(directory_path)

# # Print the file names
# for file_name in files:
#     print(file_name)
def get_random_photo():
    return files[generate_random_integer(len(files))]
# print(len(files))
# print(files[generate_random_integer(len(files))])

# print(get_random_photo())