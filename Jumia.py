import requests
from bs4 import BeautifulSoup

jumia = requests.get("https://www.jumia.co.ke/mlp-pay-day/")
#print(jumia.text)
src = jumia.content
soup = BeautifulSoup(src, 'lxml')
#product names
product_name = soup.findAll('h3', class_='name')
for name in product_name:
    pass
for element in product_name:
    product_name = element.get_text(strip=True)
    print(f"product name: {product_name}")


#product price
product_price = soup.findAll('div', class_='prc')
for price in product_price:
    pass
for element in product_price:
    product_price = element.get_text(strip=True)
    print(f"product price: {product_price}")

#product rating
product_rating = soup.findAll('div', class_="rev")
for rating in product_rating:
    pass
for element in product_rating:
    product_rating = element.get_text(strip=True)
    print(f"product rating: {product_rating}")


#product discount
product_discount = soup.findAll('div', class_="bdg _dsct _sm")
for discount in product_discount:
    pass
for element in product_discount:
    product_discount = element.get_text(strip=True)
    print(f"product discount: {product_discount}")


#collects all divs with the name,price,rating and discount
src = jumia.content
soup = BeautifulSoup(src, 'lxml')

divs = soup.findAll('div', class_='info')
for info in divs:
    print(info.prettify())

print()






