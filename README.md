# News Headlines Web Scraper

This is a simple Python script that scrapes the top news headlines from a public news website (BBC News by default) and saves them into a `.txt` file.

## Objective

- Scrape top headlines from a news website.
- Parse HTML content using `BeautifulSoup`.
- Save the extracted headlines to a text file.
- Automate basic data collection from a public site.

---

## Tools & Libraries Used

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

---

## Installation

1. **Clone the repository** (or download the `.py` file):
   ```bash
   git clone https://github.com/yourusername/news-headline-scraper.git
   cd news-headline-scraper

Install the required packages:

pip install requests beautifulsoup4

How to Run

1.Make sure you're in the same folder as news_scraper.py.
2.Run the script using Python:

python news_scraper.py

3.Once completed, a file named headlines.txt will be created in the same folder, containing the list of scraped headlines.

 How It Works
 
1. Sends an HTTP GET request to the target website using requests.
2. Parses the HTML response using BeautifulSoup.
3. Extracts all headlines from <h2 tags.
4. Saves the headlines into a clean .txt file.

Output Example (headlines.txt)

1. Global Markets Slide on Economic Fears
2. India Launches New Moon Mission
3. Weather Alert: Heavy Rains Expected in Northeast

 Legal Disclaimer

 This project is for educational purposes only. Always check a website’s robots.txt and Terms of Service before scraping. Respect the website’s data usage policies.


 Future Enhancements

1. Support for multiple news sites
2. Export headlines to .csv or .json
3. Schedule automated runs with cron or Task Scheduler
4. Add GUI using Tkinter or Streamlit


Author
Deepshikha Patidar
