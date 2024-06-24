from os import listdir
from os.path import isfile, join

new_string = ""
file_name=""
new_file_name=""

with open(file_name, 'r+') as f:
        data = f.read()
        print(data)
        new_string = data.replace('\n', ' ') # or whatever modifications are needed

with open(new_file_name, 'w+') as f:
        f.write(new_string)
