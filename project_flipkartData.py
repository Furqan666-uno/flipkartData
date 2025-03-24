import requests
from bs4 import BeautifulSoup

# List to store product details
product_names = []
prices = []

for page in range(1, 11):
    url = f'https://www.flipkart.com/search?q=mobiles+under+30000+rupees&otracker=search&otracker1=search&marketplace=FLIPKART&page={page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    boxes = soup.find_all('div', class_='_1AtVbE') # Find all the product boxes
  
    for box in boxes:
        name = box.find('a', class_='IRpwTa') 
        if name:
            product_names.append(name.get_text())
    
    for box in boxes:
        price = box.find('div', class_='_30jeq3')  # Product price
        if price:
            prices.append(price.get_text())
    
    print(f"Scraped page {page} - {len(product_names)} products")

print("\nProduct Names:")
for name in product_names:
    print(name)

print("\nPrices:")
for price in prices:
    print(price)
