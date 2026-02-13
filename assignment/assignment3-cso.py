import requests

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/CSV/1.0/en"

response = requests.get(url)
response.raise_for_status()

with open("cso.json", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Saved to cso.json")