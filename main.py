# import requests
# from bs4 import BeautifulSoup

# proxies = {
#    "http": "http://38.154.227.167:3128",
#     "https": "https://38.154.227.167:3128",
# }

# url = "http://results.ietdavv.edu.in/"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# try:
#     req = requests.get(url,headers=headers)  # Timeout set to 10 seconds
#     req.raise_for_status()  # Raise an exception for HTTP errors
#     soup = BeautifulSoup(req.text, "html.parser")  # Corrected "html.parser"
#     print(soup.prettify())
# except requests.exceptions.RequestException as e:
#     print("Error:", e)


import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://115.240.90.163",
    "https": "http://115.240.90.163",
}

url = "http://results.ietdavv.edu.in/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# Generate a list of roll numbers from 21T51101 to 21T51170
roll_numbers = ['21T511{:02d}'.format(i) for i in range(1, 71)]

for roll_number in roll_numbers:
    try:
        # Submit a POST request with the roll number
        payload = {'roll_number': roll_number}  # Adjust payload according to the form parameters
        req = requests.post(url, headers=headers, proxies=proxies, data=payload)
        req.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the response HTML
        soup = BeautifulSoup(req.text, "html.parser")
        
        # Extract data from the response using BeautifulSoup
        # Example: result = soup.find('div', {'class': 'result'}).text
        
        # Print or store the extracted data
        print(f"Data for roll number {roll_number}: {result}")
        
    except requests.exceptions.RequestException as e:
        print("Error:", e)
