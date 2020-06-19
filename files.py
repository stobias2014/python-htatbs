#!/bin/python3

from pathlib import Path


myFiles = ["names.txt", "numbers.txt", "sodas.txt"]

for filename in myFiles:
    print(Path(r"~/Desktop/python/python-htatbs", filename))

print("cwd: {0} ".format(Path.cwd()))
print("home: {0} ".format(Path.home()))

print("Creating a directory....")
# if path exists
if not Path("./folder").exists():
    Path("{0}/folder".format(Path.cwd())).mkdir()

p = Path("./folder/names.txt")

p.write_text("Saul, Brenda, Kareli")

print(p.read_text())

number_file = open("./folder/numbers.txt")

number_file_content = number_file.read()

print("Content: {0}".format(number_file_content))

number_file.close()

number_file = open("./folder/numbers.txt", 'a')

number_file.write("\n12345")

number_file.close()

number_file = open("./folder/numbers.txt")

number_file_content = number_file.readlines()

print("Content: {0} ".format(number_file_content))



