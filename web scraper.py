import requests
from bs4 import BeautifulSoup

# Step 1: Choose a public news website
URL = "https://www.theguardian.com/international"   # You can replace with another public site

# Step 2: Fetch the HTML content
response = requests.get(URL)

# Check response
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Extract headlines (BBC uses <h2> for many headlines)
    headlines = []
    for h2 in soup.find_all("h2"):
        text = h2.get_text(strip=True)
        if text:  # avoid empty strings
            headlines.append(text)

    # Step 4: Save headlines into a .txt file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines, 1):
            file.write(f"{i}. {headline}\n")

    print("✅ Headlines scraped and saved to headlines.txt")
else:
    print(f"⚠ Failed to fetch page. Status code: {response.status_code}")