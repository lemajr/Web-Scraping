import os
import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch the webpage
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find all quotes
quotes = soup.find_all("span", class_="text")

# Step 3: Create the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Step 4: Write quotes to a CSV file
file_path = os.path.join("data", "quotes.csv")
with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote Text"])
    for quote in quotes:
        writer.writerow([quote.text])

print(f"Quotes saved to {file_path}")
