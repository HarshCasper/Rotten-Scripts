import os


def searchFolder(location, min_file_size):
    fileNotFound = 0
    filesFoundCount = 0
    total_size = 0

    print(f"Files larger than {min_file_size:.2f} MB in location: {location}")
    for foldername, subfolders, filenames in os.walk(location):
        for filename in filenames:
            try:
                actual_size = os.path.getsize(os.path.join(foldername, filename))
                if min_file_size * 1024 ** 2 <= actual_size:
                    print(
                        f"{foldername}\\{filename} - " f"{(actual_size/1024**2):.2f} MB"
                    )
                    yield foldername, filename, actual_size
                    filesFoundCount += 1
                    total_size += actual_size
            except FileNotFoundError:
                fileNotFound += 1
                print(f"FileNotFoundError: {filename}")

    print(f"Files found: {filesFoundCount}")
    print(f"Total size: {(total_size/1024**2):.2f} MB")
    if fileNotFound > 0:
        print(f"FileNotFoundErrors: {fileNotFound}")


if __name__ == "__main__":

    while True:
        location = input("Where would you like to search? ")
        if os.path.exists(location):
            break
        else:
            print("Please enter a valid path.")
    while True:
        try:
            min_file_size = float(input("Please enter file size in MB: "))
            break
        except ValueError:
            print("Please enter numeric input only.")

    searchFolder(location, min_file_size)

    for foldername, filename, actual_size in searchFolder(location, min_file_size):
        print(f"{foldername}\\{filename} - {(actual_size/1024**2):.2f} MB")
