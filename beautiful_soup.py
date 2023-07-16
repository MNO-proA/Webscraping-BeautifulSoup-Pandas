import requests

from bs4 import BeautifulSoup

import pandas as pd


url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url)

soup = BeautifulSoup(r.text, features="lxml")

product_tags = soup.find_all("a", class_= "title")

# print(product_tags)

product_names = []

for i in product_tags:
    name:str = i.text
    product_names.append(name.strip("."))

# print(product_names)

price_tags = soup.find_all("h4", class_ = "pull-right price")

priceList = []

for i in price_tags:
    price = i.text
    priceList.append(price)

# print(priceList)

description_tags = soup.find_all("p", class_ = "description")

descriptionList = []

for i in description_tags:
    des = i.text
    descriptionList.append(des)

# print(descriptionList)


reviews_tags = soup.find_all("p", class_ = "pull-right")

reviewsList = []

for i in reviews_tags:
    rev = i.text
    reviewsList.append(rev)

# print(reviewsList)


df = pd.DataFrame({"Product_name":product_names, "Price":priceList, "Description":descriptionList, "Reviews":reviewsList})

df.to_csv("product_details.csv")