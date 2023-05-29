"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os


if __name__ == '__main__':
    text = []

    # I need to delete .DS file, because it is automatically created on macOs
    os.remove('files/.DS_Store')

    # read
    entries = os.listdir('files/')
    for entry in entries:
        with open(f'files/{entry}', 'r') as f:
            text.append(f.read())

    # write
    with open('files/result.txt', 'x', encoding="utf-8") as f:
        text_to_file = ', '.join(text)
        f.write(text_to_file)
