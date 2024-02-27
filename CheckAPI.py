import requests

url = "http://localhost:8090/api/metalakes"

payload={}
headers = {
  'Accept': 'application/vnd.gravitino.v1+json',
  'Authorization': 'Bearer <TOKEN>'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
# {"code":0,"metalakes":[{"name":"metalake_demo","comment":"comment","audit":{"creator":"anonymous","createTime":"2024-02-26T18:11:13.777Z"}}]}