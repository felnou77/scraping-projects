# Better not using internet during scrapping to keep loading functioning smoothly
# Install dependencies amd make sure to activate your virtual environment  
from playwright.sync_api import sync_playwright
from scrolling_helpers import full_scroll 

with sync_playwright() as p:
    #(headless=False) to keep an eye on how your script is functionning otherwise if it's quick and straightforward True
    browser = p.chromium.launch(headless=False)  
    page = browser.new_page()
    page.goto("https://store.platraw.com/ar", timeout=80000)

    page.get_by_role("button", name="كل الفئات").click()
    page.wait_for_timeout(3000)
    
    # We retrieve the category names to iterate on them 
    categories_elements = page.query_selector_all("div.categoryCard")
    category_names = [el.query_selector("p.NavbarCategories_categoryName__tVzjU").inner_text() for el in categories_elements]
    print(f"{len(category_names)} categories detected")
    
    # Click again to close the menu
    page.get_by_role("button", name="كل الفئات").click()
    
    # Empty list to store product information
    produits = []

    for name in category_names[2:3]:

        # Open the menu at each iteration
        page.get_by_role("button", name="كل الفئات").click()
        page.wait_for_selector("div.categoryCard")
        
        # Optional: a quick break
        page.wait_for_timeout(1000)

        # Dynamic element search by text
        cat = page.query_selector(f'div.categoryCard:has-text("{name}")')

        print(f"🔄 Processing category : {name}")
        cat.click()
        while True :

            page.wait_for_selector("a.Product_cardTitleLink__qDBP1")
            page.wait_for_selector("div.Product_cardImage__R1CCS")
            page.wait_for_timeout(8000)
            full_scroll(page)

            products_name  = page.query_selector_all("a.Product_cardTitleLink__qDBP1")
            products_image = page.query_selector_all("div.Product_cardImage__R1CCS")
            print(f"🛒 {len(products_name)} products found for :  {name}")

            for title, image_url in zip(products_name,products_image) : 
                title      = title.inner_text()
                image_url = image_url.query_selector("img").get_attribute("src")

                produits.append({
                'Category' : name,
                'Title'    : title,
                'Image_URL': image_url
                })

                print(f"✅ product informations retrieved")
            
            next_btn = page.query_selector("li.page-item:last-child")
            
            if "disabled" in next_btn.get_attribute("class"):
                print("⛔ Last page reached")
                break
            else: 
                next_btn.click()
                print("➡️ Go to next page...")
                page.wait_for_timeout(7000)

    input("Press Enter to exit…")
    browser.close()