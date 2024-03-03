import os


def list(path):
    try:
        n = os.listdir(path)
        directories = [i for i in n if os.path.isdir(os.path.join(path, n))]
        print("Directories : ", directories)
        files = [i for i in n if os.path.isfile(os.path.join(path, n))]
        print("Files : ", files)
        all = n
        print("Entries : ", all)
    except FileNotFoundError:
        print(f"'{path}' not found")
    except PermissionError:
        print(f"No way to '{path}'.")


specified_path = 'the way to your directory'
list(specified_path)