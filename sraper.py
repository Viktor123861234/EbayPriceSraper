import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import random
import json

# Загрузка настроек
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

BASE_URL = config["base_url"]
SEARCH_QUERY = config["search_query"]
MAX_PAGES = config["max_pages"]
HEADERS = {"User-Agent": config["user_agent"]}
OUTPUT_FILE = config["output_file"]

DELAY_MIN = config["delay_seconds_min"]
DELAY_MAX = config["delay_seconds_max"]

FILTER_BUY_IT_NOW = config["filter_buy_it_now"]
FILTER_CONDITION = config["filter_condition"]  # Пример: "New"

def get_ebay_items(page=1):
    params = {
        "_nkw": SEARCH_QUERY,
        "_pgn": page
    }
    if FILTER_BUY_IT_NOW:
        params["_sop"] = "12"  # Buy It Now сортировка
    if FILTER_CONDITION:
        params["LH_ItemCondition"] = FILTER_CONDITION

    response = requests.get(f"{BASE_URL}/sch/i.html", headers=HEADERS, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select(".s-item")
    results = []

    for item in items:
        title_tag = item.select_one(".s-item__title")
        price_tag = item.select_one(".s-item__price")
        link_tag = item.select_one(".s-item__link")

        if not title_tag or not price_tag or not link_tag:
            continue

        title = title_tag.text.strip()
        price = price_tag.text.strip()
        link = link_tag["href"].split("?")[0]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        results.append({
            "Title": title,
            "Price": price,
            "Link": link,
            "Scan date": date
        })

    return results

def main():
    all_results = []

    for page in range(1, MAX_PAGES + 1):
        print(f"[INFO] Parsing a page {page}")
        try:
            items = get_ebay_items(page)
            all_results.extend(items)
        except Exception as e:
            print(f"[ERROR] Error on page {page}: {e}")
        time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))

    df = pd.DataFrame(all_results)
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"[DONE] Saved {len(df)} items to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
