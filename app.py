import requests
import json
import csv

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

response = requests.get(url)
data = response.json()

# 存成 JSON
with open("crypto.json", "w") as f:
    json.dump(data, f, indent=4)

# 存成 CSV
with open("crypto.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "symbol", "current_price"])
    
    for coin in data:
        writer.writerow([
            coin["name"],
            coin["symbol"],
            coin["current_price"]
        ])

print("資料儲存完成")