import hashlib
import os

def calculate_sha1(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha1.update(chunk)
    return sha1.hexdigest()

def file_info(file_path):
    if not os.path.exists(file_path):
        return None

    file_size = os.path.getsize(file_path)
    sha1_hash = calculate_sha1(file_path)

    return {
        "sha1": sha1_hash,
        "size": file_size
    }

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")

    result = file_info(file_path)

    if result:
        print('{' + f'\n\t"sha1": "{result["sha1"]}",\n\t"size": {result["size"]}\n' + '}')
    else:
        print("File not found.")
