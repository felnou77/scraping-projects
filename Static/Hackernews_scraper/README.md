# HackerNews Scraper 📰

This project is a simple web scraper that collects the 50 top articles from [Hacker News](https://news.ycombinator.com/), including their titles, links, authors, time posted and vote scores.

It was built to practice static web scraping using Python, `requests`, `BeautifulSoup`, and `pandas`.

Note that the data are recorded on 07/06/2025

---

## 🔧 Technologies Used

- Python 3.x
- `requests` – to send HTTP requests
- `beautifulsoup4` – for parsing HTML content
- `pandas` – for data manipulation and saving to CSV

---

## 📌 Features

- Extracts the title of each top article 
- Extracts the corresponding link, author and date
- Extracts the score (number of upvotes)
- Stores the data in a clean xlsx file for analysis or archiving

---

## 📂 Project Structure

Hackernews_scraper/
├── hackernews_scraper.py   # Main scraping script
├── data/
│ └── hackernews_data.xlsx  # Output data file
└── README.md               # Project documentation
