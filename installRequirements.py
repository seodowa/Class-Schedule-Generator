import os

# this script assumes that you have Python 3.10+ and pip installed
# if you don't have those installed yet, go to python.org and
# install the latest version of Python (MAKE SURE TO ADD TO PATH)

with open("requirements.txt", "r") as requirements:
    lines = requirements.readlines()
    reqs = [line.strip() for line in lines]
    for arg in reqs:
        command = f"pip3 install {arg}"
        if os.system(command) != 0:
            print(f"Failed to execute command {command}.")
            exit(-1)