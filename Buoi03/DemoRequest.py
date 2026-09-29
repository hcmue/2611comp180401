import requests
import json

# Ví dụ 1: Call trang web ===> html code
# result = requests.get("https://hcmue.edu.vn")
# print(result.status_code)
# print(result.text)

# Ví dụ 2: Call API ==> json
# rs = requests.get("https://dummyjson.com/products")
# print(rs.status_code)
# if rs.status_code == 200:
#     jsobj = rs.json()
#     print(json.dumps(jsobj, indent=4))

# VD3
data = {"username":"9898","password":"9898"}
headers = {
    "clientid": "hcmue",
    "apikey": "hcmuepscRBF0zT2Mqo6vMw69YMOH43IrB2RtXBS0EHit2kzvL2auxaFJBvw=="
}
rs = requests.post(
    'https://onlineapi.hcmue.edu.vn/api/authenticate/authpsc',
    data=data,
    headers=headers
)
print(rs.status_code)