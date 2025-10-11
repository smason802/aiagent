import os

def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        path = os.path.abspath(os.path.join(working_directory, directory))
        if not path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(path):
            return f'Error: "{directory}" is not a directory'
        file_list = os.listdir(path)
        return '\n'.join(list(map(lambda file: f'{file}: file_size={os.path.getsize(os.path.join(path, file))} bytes, is_dir={os.path.isdir(os.path.join(path, file))}', file_list)))
    except Exception as e:
        return f'Error: {e}'