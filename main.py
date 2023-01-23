from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

url = 'https://criptoya.com/'
response = requests.get(url)
print(response)

src = response.content

soup = BeautifulSoup(src, 'html.parser')