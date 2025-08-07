import requests
from bs4 import BeautifulSoup

url = 'https://www.hindustantimes.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
response.raise_for_status()  # Should not raise 401 if allowed
soup = BeautifulSoup(response.text, 'html.parser')

# Continue with parsing...


# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find headline tags (you may need to adjust the tag/class for other sites)
headlines = soup.find_all('h2')

# Extract text headlines
headline_texts = [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]

# Optional: Remove duplicates and keep only the top 10
headline_texts = list(dict.fromkeys(headline_texts))[:10]

# Write the headlines to a .txt file
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for headline in headline_texts:
        file.write(headline + '\n')

print("Headlines have been saved to headlines.txt")
