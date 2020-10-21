import requests
from bs4 import BeautifulSoup

user_budget = int(input("Enter your budget: "))

content = requests.get("https://www.johnlewis.com/browse/home-garden/plants-planting/pots-planters/_/N-5urc").content
soup = BeautifulSoup(content)
element = soup.findAll("span", {"class": "product-card__price-span", "data-test": "product-card__price product-card__price--current"})
price = element.text.strip()
price_no_currency = price[1:]
price_float = float(price_no_currency)
if price_float > user_budget:
    print("The price of this item is more than your budget")
else:
    print("You can afford this item")