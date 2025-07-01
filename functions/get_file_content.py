import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):

    # creates an absolute path of the working directory
    abs_working_dir = os.path.abspath(working_directory)

    # appends the file path to the absolute working directory
    # again, if the file path is outside of the working directory, then the file path will override it
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    # checks if the file path is inside the working directory
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # checks if the file path is a file
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    # passes all checks; the file path is a file that's inside the working directory
    try:

        # opens the contents of the file and reads it up to the 10,000th character
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            # if the file size exceeds the MAX_CHARS limit, return a the file contents with the truncation string
            # else, return the file contents
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                file_content_string += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            return file_content_string

    # catches errors raised by the standard library functions
    except Exception as e:
        return f"Error reading file: {e}"
