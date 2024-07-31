import requests

response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

res=response.json()
for i in range(len(res)):
    print(res[i]["user"]["login"])