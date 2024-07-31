import os

folders=input("enter the folder name list with spaces in between : ").split(" ")

for folder in folders:
    try:
        file=os.listdir(folder)
    except FileNotFoundError:
        print(f"Wrong folder name {folder}, Enter a valid folder name")
        continue
    
print(file)
# print(os.getenv("password"))