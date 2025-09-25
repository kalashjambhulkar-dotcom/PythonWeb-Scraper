News Headline Scraper
A simple Python script to automate the extraction of top news headlines from public news websites.
The code uses requests to fetch HTML content and BeautifulSoup to parse and extract headlines (from <h2> tags).
Scraped headlines are saved into a cleanly-formatted headlines.txt file for further analysis or reference.

Features:

Fetches news headlines from any site supporting standard HTML structure

Output saved as a numbered list to a .txt file

Easily customizable to adapt headline selectors (<h2>, <h3>, etc.) for different sites

Technologies: Python, requests, BeautifulSoup
How to use:

Clone the repository

Install dependencies with pip install requests beautifulsoup4

Run the script to generate a fresh list of headlines

Sample use-case:
Track breaking news or automate monitoring of multiple sites using a shared workflow.
