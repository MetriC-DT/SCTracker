import os

directory = os.path.dirname(__file__)
this_file_name = os.path.basename(__file__)

for f in os.listdir(directory):
    if len(f) > 3 and f[-3:] == '.py' and f != this_file_name:
        with open(directory + '/' + f, 'r') as script:
            exec(script.read())