import requests
from bs4 import BeautifulSoup
import pandas as pd

URL  = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)


soup      = BeautifulSoup(page.content, "html.parser")
results   = soup.find(id="ResultsContainer") # not necessary ! just narrowing down the HTML content ^^
job_cards = results.find_all("div", class_= "card-content")


jobs=[]
for card in job_cards :
             
    title    = card.find("h2", class_= "title").get_text(strip=True)
    company  = card.find("h3", class_="company").get_text(strip=True)
    location = card.find("p", class_="location").get_text(strip=True)
    time     = card.find("time").get_text(strip=True)
    link     = card.find("a", string=lambda text: "apply" in text.lower())["href"]
    description_page = requests.get(link)
    description_results = BeautifulSoup(description_page.content, 'html.parser').find(id="ResultsContainer")
    # only find down here and not find_all since find get acces to the first element as shown in the DOM
    description =description_results.find("p").get_text(strip=True)
     
    jobs.append({
    'Title'      : title, 
    'Company'    : company, 
    'Location'   : location,
    'Date'       : time, 
    'Link'       : link,
    'Description': description
    })
            

df = pd.DataFrame(jobs)
df.to_excel("fakejobs_data.xlsx", index=False)







