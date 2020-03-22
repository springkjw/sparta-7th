import requests
# requests.get(url)
# requests.post(url, data={"id": "username"})
r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']
for gu in gus:
    gu_name = gu["MSRSTE_NM"]
    misae_value = gu["IDEX_MVL"]
    if misae_value < 100:
        print(gu_name)