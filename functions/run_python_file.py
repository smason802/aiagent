import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(working_directory, file_path))
        if not path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(path):
            return f'Error: File "{file_path}" not found.'
        if not path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        commands = ["python", path]
        if args:
            commands.extend(args)
        process = subprocess.run(commands, timeout=30, capture_output=True, text=True, cwd=abs_working_dir)
        rtrn_string = f''
        if process.stdout:
            rtrn_string+= f'STDOUT: {process.stdout}\n'
        if process.stderr:
            rtrn_string+= f'STDERR: {process.stderr}\n'
        if process.returncode != 0:
            rtrn_string+= f'Process exited with code {process.returncode}'
        return rtrn_string
    except Exception as e:
        return f'Error: {e}'