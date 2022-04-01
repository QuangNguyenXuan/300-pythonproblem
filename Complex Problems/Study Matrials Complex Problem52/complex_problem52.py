import urllib.request

site = urllib.request.urlopen("https://www.jafricode.com")
code = site.getcode()
print(code)