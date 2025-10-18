from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def google_search(query, num_results=5, headless=False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://www.google.com")
        
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for results container
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        
        # Extract results
        results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
        
        print(f"Top {num_results} results for '{query}':\n")
        for i, result in enumerate(results[:num_results], 1):
            title = result.find_element(By.TAG_NAME, 'h3').text
            link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
            print(f"{i}. {title}\n   {link}\n")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    user_query = input("Enter search query: ")
    try:
        count = int(input("Number of results to display: "))
    except ValueError:
        count = 5
    headless_mode = input("Run in headless mode? (y/n): ").strip().lower() == 'y'
    
    google_search(user_query, num_results=count, headless=headless_mode)
