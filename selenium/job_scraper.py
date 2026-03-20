import csv
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

JOB_SOURCES = [
    {"company": "Shopify",  "platform": "Greenhouse", "url": "https://www.shopify.com/careers", "type": "greenhouse"},
    {"company": "Stripe",   "platform": "Greenhouse", "url": "https://stripe.com/jobs",          "type": "greenhouse"},
    {"company": "Notion",   "platform": "Lever",      "url": "https://www.notion.so/careers",    "type": "lever"},
]

OUTPUT_FILE = "data/raw/job_links.csv"


def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def collect_links():
    driver = get_driver()
    all_links = []

    for source in JOB_SOURCES:
        logger.info(f"Loading {source['company']} — {source['url']}")
        try:
            driver.get(source["url"])
            time.sleep(3)
            links = driver.find_elements(By.TAG_NAME, "a")
            for link in links:
                href = link.get_attribute("href") or ""
                text = link.text.strip()
                if href and text:
                    all_links.append({
                        "company":  source["company"],
                        "platform": source["platform"],
                        "title":    text,
                        "url":      href,
                    })
            logger.info(f"  Collected {len(links)} links from {source['company']}")
        except Exception as e:
            logger.warning(f"  Failed on {source['company']}: {e}")

    driver.quit()

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["company", "platform", "title", "url"])
        writer.writeheader()
        writer.writerows(all_links)

    logger.info(f"Saved {len(all_links)} links to {OUTPUT_FILE}")


if __name__ == "__main__":
    collect_links()