# 🛍️ Platraw E-commerce Scraper (Dynamic Website)

This project is a **freelance web scraping solution** developed for a client based in **Saudi Arabia**, targeting the [Platraw](https://store.platraw.com/ar) e-commerce platform.  
It demonstrates how to handle scraping from **dynamic websites** using `Playwright`, with special care given to **lazy loading** and **pagination**.

---

## 🚀 Key Features

- ✅ Built using **Playwright** (`sync_api`)
- ✅ Handles **dynamic content loading**
- ✅ Scrolls automatically to trigger **lazy loading**
- ✅ Navigates through **all pages** of a selected category
- ✅ Extracts:
  - Product **titles**
  - Product **images**
  - Product **category**

---

## ⚙️ Technologies Used

- [Python 3.x](https://www.python.org/)
- [Playwright (Python)](https://playwright.dev/python/)
- Custom scrolling utility to handle lazy loading

---

## 🧠 What This Script Does

1. Launches a Chromium browser (optionally headless)
2. Opens the Platraw website and accesses the category menu
3. Iterates through a list of categories (dynamic DOM elements)
4. For each product:
   - Scrolls down the page to trigger content loading
   - Retrieves product title and image URL
5. Navigates through all paginated results
6. Stores the data in xlsx file 