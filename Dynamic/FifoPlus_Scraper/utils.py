from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.fifoplus.com/", timeout=80000)

    # 💡 Manually select the location (e.g., click on Riyadh) to bypass the geolocation pop-up
    input("🖱️ Sélectionne manuellement une ville, puis appuie sur Entrée...")

    # ✅ Save the current browser state (including cookies & localStorage) to a JSON file.
    # This helps avoid the geolocation pop-up in future sessions by loading stored data.
    context.storage_state(path="fifoplus_state.json")

    browser.close()