import os

path = 'uploads'
files = os.listdir(path)

for file in files:
    print(file)