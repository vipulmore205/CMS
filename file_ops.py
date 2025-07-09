# file_ops.py

FILE_NAME = "college_data.txt"

def read_file():
    try:
        with open(FILE_NAME, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def write_file(lines):
    with open(FILE_NAME, "w") as f:
        f.writelines(lines)

def append_to_file(record):
    with open(FILE_NAME, "a") as f:
        f.write(record + "\n")
