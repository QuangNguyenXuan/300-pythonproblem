import requests
site  = "https://www/google.com"
page = requests.get(url=site)
page_html = page.text()
print(page_html)