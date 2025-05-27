Credit Card Scraper
-

This project was my attempt at creating a website scraper to collect the name and info of the best credit cards according to Nerd Wallet. It creates a text file and puts the info of the credit cards.

Project Structure:
-
- credit_card_scraper.py - Does all the work and creates the file.

Tools and Libraries Used:
-
- Selenium
- BeautifulSoup4
- Time

Steps Preformed:
-
1. Create a headless Chrome client
2. Load the page
3. Parse the info with bs4
4. Find every single element with the class of the credit card block
5. For every single credit card, find the name and info
6. Write the name, info label, and info to a text file

How To Run:
-
1. Make sure you have Python installed
2. Install dependencies: `pip install selenium bs4`
3. Run script: `python credit_card_scraper.py`

Notes:
- 
- I might expand this to scrape more info from more pages that NerdWallet has