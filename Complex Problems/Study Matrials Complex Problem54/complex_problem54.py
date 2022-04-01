from bs4 import BeautifulSoup
import requests

url   = "https://www/google.com"
req = requests.get(url)
text = BeautifulSoup(req.text, "html.parser")
t = text.title
print(t)