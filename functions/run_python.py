import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    # converts the working directory and file path to their absolute versions
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # checks if the file path is in the working directory
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # checks if the file path exists
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    # checks if the file path is a python file
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    # try catch block to catch any exceptions when running the subprocess
    try:
        # NOTE: the "args" in "subprocess.run()" is the terminal command (e.g. "ls")
        commands = ["python", abs_file_path]  # "file_path" probably works fine here

        # the "args" in this code represents the argument after "python <name>.py"
        if args:
            commands.extend(args)

        # the "text" parameter converts the raw output to a formatted output (just like how it would look like if you ran it from the terminal yourself)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir,
        )

        # prints the output, error, or code error if they exist
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        # prints the string if no output is produced
        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
