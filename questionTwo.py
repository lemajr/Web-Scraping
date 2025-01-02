import os
import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch the webpage
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find all authors
authors = soup.find_all("small", class_="author")

# Step 3: Create the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Step 4: Write authors to a CSV file
file_path = os.path.join("data", "authors.csv")
with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Author Name"])
    for author in authors:
        writer.writerow([author.text])

print(f"Authors saved to {file_path}")
