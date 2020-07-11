from hashlib import md5
from os.path import join


def hash_strings_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_read:
        for line in file_read:
            hashed_line = md5(line.encode()).hexdigest()
            yield hashed_line


for item in hash_strings_from_file('output/countrylink.txt'):
    print(item)
