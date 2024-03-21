import requests
from bs4 import BeautifulSoup
import time

# Define the proxy
proxy = {
    "http": "http://180.183.157.159",
    "https": "https://180.183.157.159",
}

# Initialize an empty dictionary to store results
results = {}

# Base URL of the website to scrape
base_url = "http://results.ietdavv.edu.in/DisplayStudentResult?rollno={}&typeOfStudent=Regular"

# Loop through roll numbers
for roll_number in range(2115101, 2115102):  # Assuming you want to scrape from 21T5101 to 21T5170
    # Construct URL for the current roll number
    url = base_url.format(roll_number)
    print("Fetching data for URL:", url)  # Print the URL for debugging purposes
    
    try:
        # Send an HTTP GET request to the website using the proxy
        response = requests.get(url, proxies=proxy, verify=False)
        
        # Add a delay to avoid sending too many requests too quickly
        time.sleep(1)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML code using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the required data and store it in the results dictionary
            result = soup.find("font", color="#4B0082")
            sgpa = soup.find("b")
            
            if result and sgpa:
                # Store the result for the current roll number in the dictionary
                results[roll_number] = {"Result": result.text, "SGPA": sgpa.text}
            else:
                print("Data not found for roll number:", roll_number)
        
        else:
            print("Failed to retrieve data for roll number:", roll_number)
    
    except Exception as e:
        print("An error occurred:", e)

# Print the scraped results
for roll_number, result_data in results.items():
    print("Roll Number:", roll_number)
    print("Result:", result_data["Result"])
    print("SGPA:", result_data["SGPA"])
    print()
