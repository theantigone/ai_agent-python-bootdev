import os


def write_file(working_directory, file_path, content):

    # convert working directory and file path to their absolute paths
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

    # checks if the file path is inside the working directory
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # checks if the file path exists
    if not os.path.exists(abs_file_path):
        try:

            # creates the directory; if it exists, continue
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

        except Exception as e:
            return f'Error: creating directory "{os.path.dirname(file_path)}": {e}'

    # checks if file_path is a file
    if os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'

    try:

        # overwrites file_path's contents to content
        with open(abs_file_path, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    # checks if any errors have been raised
    except Exception as e:
        return f'Error: writing to file "{file_path}": {e}'
