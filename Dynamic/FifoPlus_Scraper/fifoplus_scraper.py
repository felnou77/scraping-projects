from playwright.sync_api import sync_playwright
import pandas as pd
from helpers import full_scroll 

with sync_playwright() as p:
    # Load saved state
    browser = p.chromium.launch(headless=False) # Useful for debugging
    context = browser.new_context(storage_state="fifoplus_state.json")

    page = context.new_page()
    page.goto("https://www.fifoplus.com/", timeout=80000)
    page.wait_for_timeout(6000)
   

    # We retrieve the category names to iterate on them 
    categories_elements = page.query_selector_all("div.owl-item.active")
    categories_elements = categories_elements[:9]

    category_names = [el.query_selector("span").inner_text() for el in categories_elements]

    # Empty list to store product information 
    produits = []

    for i, name in enumerate(category_names) :
        page.wait_for_selector("div.owl-item.active")
        page.wait_for_timeout(4000)
        categories_elements = page.query_selector_all("div.owl-item.active")
        categories_elements = categories_elements[:9] 
        categories_elements[i].click()
        print(f"🔄 Processing the {i+1}ème category : {name}")

        page.wait_for_selector("select.limiter-options")
        page.wait_for_timeout(4000)
        page.locator("div.field.limiter").locator("select.limiter-options").nth(0).select_option("all")
        page.wait_for_selector("div.product-item-info")
        page.wait_for_timeout(7000)
        full_scroll(page) #images are lazy loaded so we simulate scrolling

        
        products = page.query_selector_all("div.product-item-info")
        print(f"🛒 {len(products)} found products for {name}")
        

        for j, prod in enumerate(products) : 

            print(f"🔗 Processing the product {j+1}/{len(products)}")
            title     = prod.query_selector("h2.product-item-name").inner_text()
            image_url = prod.query_selector("img.product-image-photo").get_attribute("src")

            produits.append({
                'Category'  : name,
                'Title'     : title,
                'Image_URL' : image_url
                 })

    df = pd.DataFrame(produits)
    df.to_excel("fifo_data.xlsx", index=False)

    input("🚀 Press Enter to exit…")
    browser.close()


   