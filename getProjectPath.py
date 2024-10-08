import os

def get_project_path():
    # Get the absolute path of the current script file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    

    current_directory = current_directory.replace('/', '\\')
    return str(current_directory)

# # Call the function to get the project path
project_path = get_project_path()

# Convert forward slashes to double backslashes


# Print the project path
print("Project path:", project_path)