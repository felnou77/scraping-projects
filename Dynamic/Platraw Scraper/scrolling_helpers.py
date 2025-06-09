import time

def full_scroll(page):
    
    previous_height = 0
    max_attempts = 10  # Limit the number of times we try to scroll without seeing new content (prevents infinite loop)
    attempts = 0

    while attempts < max_attempts:
        # Execute JavaScript inside the browser to scroll down by 1000 pixels
        # Then return the current full scroll height of the page
        current_height = page.evaluate("""() => {
            window.scrollBy(0, 1000);
            return document.body.scrollHeight;
        }""")

        time.sleep(2)  # Wait for 2 seconds to give the page time to load new content (lazy loading)

        if current_height == previous_height:
            # If the page height hasn't increased, count this as an unsuccessful scroll
            attempts += 1
        else:
            # If new content has been loaded (page got taller), reset attempt counter
            attempts = 0

        # Update the last recorded height for the next comparison
        previous_height = current_height