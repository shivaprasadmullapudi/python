file_path=input("Enter a file name: ")
key=input("Enter a key:")#MAX_CONNECTIONS
value=input("Enter a value: ")
def update_server_conf(file_path,key,value):
    with open(file_path,"r") as file:
        lines=file.readlines()
        
    with open(file_path,"w") as file:
        for line in lines:
            if key in line:
                file.write(key+"="+value+"\n")
            else:
                file.write(line)
                             
update_server_conf(file_path,key,value)