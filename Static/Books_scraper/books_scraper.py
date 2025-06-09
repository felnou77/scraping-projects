import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

URL      = "https://books.toscrape.com/index.html"
base_URL = "https://books.toscrape.com/catalogue/"

# A function for URL management 
def normalize_url(path):
    if path.startswith('catalogue/'):
        path = path[len('catalogue/'):] 
    return urljoin(base_URL, path)

books = []

while True:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    book_cards = soup.find_all("article", class_="product_pod")

    for book in book_cards:
        link             = book.find("h3").find("a")["href"].strip()
        description_html = BeautifulSoup(requests.get(normalize_url(link)).content, "html.parser")
        product_html     = description_html.find("div", class_="product_main")
        title            = product_html.find("h1").get_text(strip=True)
        price            = product_html.find("p", class_="price_color").get_text(strip=True)
        availability     = product_html.find("p", class_="instock availability").get_text(strip=True)
        star_rating      = product_html.find("p", class_="star-rating").get('class')[1]
        category         = description_html.find("ul", class_="breadcrumb").find_all("li")[2].find("a").get_text(strip=True)
        
        books.append({
            'Title'       : title,
            'Price'       : price,
            'Availability': availability,
            'Star rating' : star_rating,
            'Category'    : category
        })

    # Checks pagination after processing the current page 
    next_link = soup.find("li", class_="next")

    if next_link:
        next_url = next_link.find("a")["href"]
        URL = normalize_url(next_url)
    
    else:
        # No more pages ---> out of the loop
        break  

# Export or final display
df = pd.DataFrame(books)
df.to_excel("books_data.xlsx", index=False)
