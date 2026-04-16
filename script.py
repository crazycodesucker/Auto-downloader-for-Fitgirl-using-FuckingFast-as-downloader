import time
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ---- USER INPUT ----
URL = input("Enter page URL: ").strip()
DOWNLOAD_DIR = input("Enter download folder path: ").strip()

# ---- SCRAPER ----
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# find FuckingFast section
target_anchor = None
for a in soup.find_all("a"):
    if a.text and "FuckingFast" in a.text:
        target_anchor = a
        break

if not target_anchor:
    print("FuckingFast section not found")
    exit()

spoiler_div = target_anchor.find_next("div", class_="su-spoiler-content")

if not spoiler_div:
    print("Spoiler content not found")
    exit()

# extract links directly into list
URLS = []
for a in spoiler_div.find_all("a", href=True):
    href = a["href"]
    if "fuckingfast.co" in href:
        URLS.append(href)

print(f"Found {len(URLS)} links")

# ---- SELENIUM (BRAVE) ----
options = Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(driver_version="147").install()),
    options=options
)

wait = WebDriverWait(driver, 15)

# ---- HELPERS ----
def get_filename_from_url(url):
    return url.split("#")[-1] if "#" in url else None

def wait_for_download(filename):
    while True:
        files = os.listdir(DOWNLOAD_DIR)

        if any(f.endswith(".crdownload") for f in files):
            print(f"Waiting... ({filename})")
            time.sleep(10)
            continue

        if filename in files:
            print(f"Done: {filename}")
            break

        print(f"Still waiting for {filename}...")
        time.sleep(10)

# ---- DOWNLOAD LOOP ----
for url in URLS:
    filename = get_filename_from_url(url)

    if not filename:
        print(f"Skipping: {url}")
        continue

    print(f"Downloading: {filename}")

    driver.get(url)

    download_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.gay-button"))
    )

    driver.execute_script("arguments[0].click();", download_btn)

    wait_for_download(filename)

driver.quit()

print("All downloads completed 🚀")