"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    with open("files/file1.txt", mode="w", encoding="utf-8") as f:
        f.write("\n".join(words))

    with open("files/file2.txt", mode="w", encoding="cp1252") as f:
        words.reverse()
        f.write(", ".join(words))

    return words


if __name__ == '__main__':
    generate_words()
