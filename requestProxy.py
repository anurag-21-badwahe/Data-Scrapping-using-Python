import requests
from bs4 import BeautifulSoup


proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

req = requests.get("https://api64.ipify.org?format=json")
print(req.json())

