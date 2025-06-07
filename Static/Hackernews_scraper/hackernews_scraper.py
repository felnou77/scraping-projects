import requests
from bs4 import BeautifulSoup
import pandas as pd 

URL     = "https://news.ycombinator.com/news"
base_URL = "https://news.ycombinator.com/news"
exit_all = False 

# A function for URL management
def normalize_url(path): 
    return(base_URL+path)

# Scraping the last 50 news on HackerNews

news=[]
while True : 
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    title_info  = soup.find_all("span", class_="titleline")
    thread_info = soup.find_all("span", class_="subline")

    for info1, info2 in zip(title_info, thread_info):

        title  = info1.find("a").get_text(strip=True)
        link   = info1.find("a")["href"].strip()
        score  = info2.find("span", class_="score").get_text(strip=True)
        author = info2.find("a", class_="hnuser").get_text(strip=True)
        time   = info2.find("span", class_="age")['title'].strip()
        
        if len(news) < 50 : 
            news.append({
                'Title'      : title,
                'Time posted': time.split('T')[0],
                'Link'       : link,  
                'Score'      : score, 
                'Author'     : author
                })
        else :
            exit_all = True
            break
                  
    if exit_all : 
        break
    
    URL = normalize_url(soup.find("a", class_="morelink")["href"].strip())

df = pd.DataFrame(news)
df.to_excel("hakcernews_data.xlsx", index=False)