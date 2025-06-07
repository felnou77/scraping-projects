# Books gallery Scraper 📰

This project is a simple web scraper that collects the books infos from [Books to scrap](https://books.toscrape.com/), including their titles, prices, availability and much more.

It was built to practice static web scraping using Python, `requests`, `BeautifulSoup`, and `pandas`.

---

## 🔧 Technologies Used

- Python 3.x
- `requests` – to send HTTP requests
- `beautifulsoup4` – for parsing HTML content
- `pandas` – for data manipulation and saving to xlsx

---

## 📌 Features

- Extracts the title of each book
- Extracts the corresponding price, availability and star rating
- Extracts the category (history, fiction, art...)
- Stores the data in a clean CSV file for analysis or archiving

---

## 📂 Project Structure

Books_scraper/
├── books_scraper.py  # Main scraping script
├── data/
│ └── books_data.xlsx # Output data file
└── README.md         # Project documentation