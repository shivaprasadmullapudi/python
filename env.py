import os

folders=input("enter the folder name list with spaces in between : ").split(" ")

for folder in folders:
    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print(f"Wrong folder name {folder}, Enter a valid folder name")
        continue
    
    for file in files:
        print(file)
        
        
        
        
        
# print(os.getenv("password"))