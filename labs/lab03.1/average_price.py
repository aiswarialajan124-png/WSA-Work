import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

response = requests.get(URL)
books = response.json()

total = 0
count = 0

for book in books:
    price = book.get("price")
    
    if isinstance(price, (int, float)):
        total += price
        count += 1

if count > 0:
    average = total / count
    print("Average book price: ", round(average, 2))
else:
    print("No valid prices found")
