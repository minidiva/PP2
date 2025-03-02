import os
import shutil

# 1
def list_dir_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return directories, files

print("Task 1")
print(list_dir_files("c:/Users/alant/PP2 Laboratory works"))


# 2
def check_path_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK),
    }

print("\n")
print("Task 2")
print(check_path_access("c:/Users/alant/PP2 Laboratory works"))


# 3
def path_info(path):
    if os.path.exists(path):
        return os.path.dirname(path), os.path.basename(path)
    return None, None

print("\n")
print("Task 3")
print(path_info("c:/Users/alant/PP2 Laboratory works"))


# 4
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for _ in file)

print("\n")
print("Task 4")
print(count_lines("c:/Users/alant/PP2 Laboratory works/lab6/peekaboo.txt"))


# 5
def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        file.writelines("\n".join(data))

print("\n")
print("Task 5")
(write_list_to_file("c:/Users/alant/PP2 Laboratory works/lab6/peekaboo.txt", ["Now you have 1 line"]))
print("File written successfully")


# 6
def generate_text_files():
    for char in range(65, 91): # ASCII A-Z
        with open(f"{chr(char)}.txt", "w") as file:
            file.write(f"This is {chr(char)}.txt")

print("\n")
print("Task 6")
generate_text_files()
print("File generated successfully")


# 7
def copy_file(source, destination):
    shutil.copyfile(source, destination)

print("\n")
print("Task 7")
copy_file("peekaboo.txt", "copy_peekaboo.txt")


# 8
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    return False


# print("\n")
# print("Task 7")
# delete_file("peekaboo.txt")
