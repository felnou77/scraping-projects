# 🛍️ FIFOPLUS Dynamic Scraper

This is a freelance web scraping project developed for a client based in **Saudi Arabia**, targeting the **dynamic e-commerce platform** [fifoplus.com](https://www.fifoplus.com/). The main goal was to extract product information across different categories, despite the challenges posed by dynamic loading and geo-restriction mechanisms.

## 🔍 Tech Stack & Libraries

- **Playwright** (Python sync API)
- **Headless browser automation**
- Handling **pagination**, **lazy loading**, and **anti-scraping mechanisms**.

## 🚧 Geolocation Pop-up Challenge

One of the main obstacles in scraping *fifoplus.com* was the **geolocation pop-up** that appears when a user accesses the site for the first time, requiring them to manually select a city (e.g., Riyadh). This pop-up blocks all navigation and interaction until a location is chosen.

### ✅ The Workaround

To bypass this issue (and it's the first thing to do), a utility script (`utils.py`) was created to:

- Launch the browser.
- Prompt the user to manually select a city.
- Automatically **save the browser state** (cookies, localStorage, etc.) to a JSON file named `fifoplus_state.json`.

Once the state is saved, the main scraping script (`fifoplus_scraper.py`) **loads this JSON state** on launch, which allows the script to bypass the pop-up and operate as if the city has already been selected.

⚠️ **Important**: Ensure the path to `fifoplus_state.json` in your main script is correct, especially if you move files or restructure directories.
