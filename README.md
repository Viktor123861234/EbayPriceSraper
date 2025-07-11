# 🕷 eBay PriceScraper

**eBay PriceScraper** is a Python script for scraping product titles, prices, and links from eBay based on a keyword search. Fully configurable via a JSON file.

| Parameter           | Description                                         |
| ------------------- | --------------------------------------------------- |
| `base_url`          | eBay domain to use (`.com`, `.de`, `.co.uk`, etc.)  |
| `search_query`      | Keyword to search for (e.g. `"iphone 13"`, `"gpu"`) |
| `max_pages`         | Number of result pages to scrape                    |
| `delay_seconds_min` | Minimum delay between requests (in seconds)         |
| `delay_seconds_max` | Maximum delay between requests                      |
| `user_agent`        | Browser User-Agent for anti-bot evasion             |
| `output_file`       | Name of the output CSV file                         |
| `filter_buy_it_now` | `true` to scrape only "Buy It Now" listings         |
| `filter_condition`  | `"New"`, `"Used"` or `null` (no condition filter)   |


## 📦 Dependencies

Install required packages:

```bash
pip install -r requirements.txt

