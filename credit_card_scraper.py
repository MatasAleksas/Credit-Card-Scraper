"""
Scraping bot that complies a list of credit cards, their details (such as rewards, interest, etc.) and puts that into
a file. This bot is used for a bigger project involving credit cards, and I noticed there isn't a complied list of
credit cards.

Author: Matas Aleksas
Version: 1.0.0
"""
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

card_file = "cards.txt"

# Create a headless Chrome browser
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# Load page and set a timer to let the page load
driver.get("https://www.nerdwallet.com/the-best-credit-cards")
time.sleep(5)

# Parse all the info and searches the webpage for the credit card info
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

cards = soup.find_all("div", {"class": "MuiBox-root css-183afol"})

"""
Helper function that creates a credit card text file if it doesn't exist and writes specified info into it.
"""
def write_to_file(info):
    if os.path.exists(card_file):
        file = open(card_file, "a")
        file.write(info + "\n")
        file.close()
    else:
        file = open(card_file, "w")
        file.write(info + "\n")
        file.close()

# For every single card it searches for the name and the spans of the card info and their labels
for card in cards:
    title_tag = card.find("a", {"class": "MuiTypography-root MuiTypography-headline MuiLink-root MuiLink-underlineHover css-1ibrk7z"})
    info_spans = card.find_all("span", {"class": "MuiTypography-root MuiTypography-textBold css-1rcc7es"})
    info_labels = card.find_all("span", {"class": "MuiTypography-root MuiTypography-bodySmall css-1eogwqc"})

    # If the title tag exists then write it to the file
    if title_tag:
        card_name = title_tag.text.strip()
        name = f"Card Name: {card_name}"
        write_to_file(name)

    # If the info spans and info labels exist then write to file as "label: info"
    if info_spans and info_labels:
        for i in range(0, len(info_spans)):
            label = f"{info_labels[i].text.strip()}: {info_spans[i].text.strip()}"
            write_to_file(label)

    # Add a space at the end of each credit card info block
    write_to_file("")