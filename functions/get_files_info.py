import os


def get_files_info(working_directory, directory=None):

    # creates an absolute path of the working directory
    abs_working_dir = os.path.abspath(working_directory)

    target_dir = abs_working_dir

    # creates an absolute path of the working directory and directory if directory exists
    # if the directory is outside of the working directory, the directory path overrides the working directory
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))

    # checks if the target directory is inside the working directory
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # checks if the target directory is a directory
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    # continues if the target directory is a directory inside the working directory
    try:
        files_info = []

        # NOTE: os.listdir returns a list of files inside the directory
        for filename in os.listdir(target_dir):

            # returns the filename, file size, and file type
            filepath = os.path.join(target_dir, filename)

            # NOTE: this declaration is needed in case the filepath cannot be found
            file_size = 0

            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)

    # checks if the working directory is invalid
    except Exception as e:
        return f"Error listing files: {e}"
