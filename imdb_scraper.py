from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

print("----- IMDb TOP 250 Scraper -----")

url = "https://www.imdb.com/chart/top/"

# Chrome Options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

driver.get(url)
time.sleep(3)

movies = []
years = []
ratings = []

# Get all movie rows
rows = driver.find_elements(
    By.XPATH,
    "//li[contains(@class,'ipc-metadata-list-summary-item')]"
)

print("Total movies found:", len(rows))

for row in rows:
    # Movie Name
    movie_name = row.find_element(By.XPATH, ".//h3").text
    movies.append(movie_name)

    # Year
    year = row.find_element(
        By.XPATH,
        ".//span[contains(@class,'cli-title-metadata-item')]"
    ).text
    years.append(year)

    # Rating
    rating = row.find_element(
        By.XPATH,
        ".//span[contains(@class,'ipc-rating-star--rating')]"
    ).text
    ratings.append(rating)

driver.quit()

# Save CSV
df = pd.DataFrame({
    "Movie": movies,
    "Year": years,
    "Rating": ratings
})

df.to_csv("imdb_top_250.csv", index=False)

print("\n----- Scraping Completed -----\n")
print(df)