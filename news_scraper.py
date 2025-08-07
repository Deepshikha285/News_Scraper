import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    headline_tags = soup.find_all('h2')

    headlines = [tag.get_text(strip=True) for tag in headline_tags if tag.get_text(strip=True)]
    return headlines

def save_headlines_to_file(headlines, filename='headlines.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for i, headline in enumerate(headlines, 1):
            f.write(f"{i}. {headline}\n")

def main():
    url = "https://www.aajtak.in/"
    print("Fetching headlines from:", url)
    headlines = fetch_headlines(url)
    save_headlines_to_file(headlines)
    print(f"✅ {len(headlines)} headlines saved to 'headlines.txt'")

if __name__ == "__main__":
    main()
