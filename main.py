# This is a mackine learning projct based on pyhon
# Here I try to teach an ai to recognize a specifc object


from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from sklearn.linear_model import LinearRegression
import requests as req
import numpy as np
import os

query = "ball"
parsed_query = query.replace(" ", "+")
path = query.replace(" ", "_")
url = "https://www.google.com/search?q="+parsed_query+"&prmd=ivn&sxsrf=APq-WBtkfb6MVdpQPRwfkJHGKPrJORUG5A%3A1650731208769&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjlvcX6zKr3AhXPzDgGHf6kDuMQ_AUoAXoECAEQAQ&biw=491&bih=925&dpr=2.2&sfr=vfe&authuser=0"
page = urlopen(url)
soup = bs(page, "lxml")
array = []
num = 0
for link in soup.find_all("img", attrs={"class": "rg_i"}):
    if "data-src" in link.attrs:
        imglink = link.attrs["data-src"]
        print(imglink)
        img_data = req.get(imglink)
        img_code = img_data.content
        array.append(img_code)
        num += 1
    if num == 10:
        for i in array:
            predictor = LinearRegression(n_jobs=-1)
            predictor.fit(x=query, y=i)
        exit()
