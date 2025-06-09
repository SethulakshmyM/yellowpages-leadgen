import undetected_chromedriver as uc
import pandas as pd
import time
import urllib.parse
from selenium.webdriver.common.by import By


def get_leads(keyword, location, pages=1):
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("start-maximized")

    driver = uc.Chrome(options=options)

    results = []

    for page in range(1, pages + 1):
        encoded_keyword = urllib.parse.quote_plus(keyword)
        encoded_location = urllib.parse.quote_plus(location)
        url = f"https://www.yellowpages.com/search?search_terms={encoded_keyword}&geo_location_terms={encoded_location}&page={page}"

        try:
            driver.get(url)
            time.sleep(2)
            listings = driver.find_elements(By.CLASS_NAME, "result")

            for listing in listings:
                try:
                    name = listing.find_element(By.CLASS_NAME, "business-name").text
                except:
                    name = "N/A"
                try:
                    phone = listing.find_element(By.CLASS_NAME, "phones").text
                except:
                    phone = "N/A"
                try:
                    address = listing.find_element(By.CLASS_NAME, "adr").text
                except:
                    address = "N/A"

                if name != "N/A":
                    results.append({
                        "Business Name": name,
                        "Phone": phone,
                        "Address": address
                    })

        except Exception as e:
            print(f"❌ Page {page} failed: {e}")

        time.sleep(3)

    driver.quit()

    df = pd.DataFrame(results)
    df.drop_duplicates(subset=["Business Name"], inplace=True)
    return df
