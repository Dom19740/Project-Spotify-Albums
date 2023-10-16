import os

# Root folder path
root_folder = r"E:\_Music"

# Text file path to save the album list
output_file = r"album_list.txt"


def get_album_names(root_folder):
    album_names = []

    for dirpath, dirnames, filenames in os.walk(root_folder):
        for dirname in dirnames:
            album_names.append(dirname)

    return album_names


def write_to_file(album_names, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for album_name in album_names:
            file.write(album_name + "\n")


# Get album names
album_names = get_album_names(root_folder)

# Write album names to file
write_to_file(album_names, output_file)
