import time

def full_scroll(page):
    previous_height = 0
    max_attempts = 10  
    attempts = 0

    while attempts < max_attempts:
        current_height = page.evaluate("""() => {
            window.scrollBy(0, 1000);
            return document.body.scrollHeight;
        }""")
        time.sleep(2) 

        if current_height == previous_height:
            attempts += 1
        else:
            attempts = 0

        previous_height = current_height