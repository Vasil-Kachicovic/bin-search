import sys
import os.path


def get_full_path(file):
    return os.path.abspath(file)


def file_exists(file):
    return os.path.isfile(file)


def get_file_size(file):
    try:
        return os.path.getsize(file)
    except OSError:
        file_error()


def file_error():
    print(f"""Wrong filename! {file_argument} does not exist or is not a file!
If {file_argument} shoud exist, check if you have read rights!
Exiting...""")
    sys.exit(1)


def zero_arguments():
    version = "0.1"
    print(f"""You didn't supply any arguments!
Usage: python3 binSearch.py [FILE]
Version: {version}""")
    sys.exit(1)


if __name__ == '__main__':

    if len(sys.argv) == 1:
        zero_arguments()

    file_argument = sys.argv[1]
    file_path = get_full_path(file_argument)

    if file_exists(file_path) == True:
        file_size = get_file_size(file_path)
        print(f"File {file_argument} exists and has {file_size} bytes")
    else:
        file_error()
