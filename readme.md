# 🚀 Auto Downloader (FitGirl + FuckingFast)

A fully automated Python script that:

* Scrapes download links directly from a webpage
* Targets **FuckingFast** file hoster specifically
* Opens each link in **Brave browser (Selenium)**
* Clicks the download button automatically
* Waits until the file is fully downloaded before moving on

---

## ⚙️ Features

* 🔍 Automatic scraping (no manual link copying)
* ⚡ Direct integration (scrape → download in one run)
* 🧠 Smart waiting system (detects `.crdownload`)
* 🌐 Uses your **Brave browser**
* 📂 No temporary files required

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---


## ▶️ Usage

Run the script:

```bash
python script.py
```

Then enter:

```
Enter page URL: https://fitgirl-repacks.site/your-game/
Enter download folder path: E:\YourFolder
```

---

## 🧠 How It Works

1. Fetches webpage HTML using `requests`
2. Parses using `BeautifulSoup`
3. Finds:

   * `Filehoster: FuckingFast`
   * Extracts links inside `.su-spoiler-content`
4. Launches **Brave via Selenium**
5. For each link:

   * Opens page
   * Clicks download button
   * Waits until file is fully downloaded

---

## ⚠️ Important Notes

* ✔️ Brave must be installed at:

  ```
  C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe
  ```

* ✔️ Update ChromeDriver version if Brave updates:

  ```python
  ChromeDriverManager(driver_version="147")
  ```

* ❗ Script assumes download button:

  ```css
  button.gay-button
  ```

---

## ❌ Limitations

* Only works for **FuckingFast host links**
* Will fail if:

  * Website structure changes
  * Download button selector changes
  * Site blocks automation

---

## 🔥 Future Improvements

* Skip already downloaded files
* Retry failed downloads
* Multi-threaded downloads
* Auto-detect Brave version

---

## 🧩 Project Structure

```
.
├── script.py
├── requirements.txt
└── README.md
```

---

## 💡 Disclaimer

This tool is for educational purposes only.
Use responsibly and respect content ownership.

---

## 🏁 Status

✔️ Working
✔️ Automated
✔️ No manual steps

---

Made for speed ⚡ and zero effort.
