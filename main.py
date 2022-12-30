import os
import requests
import shutil
from bs4 import BeautifulSoup

POKEMONWEBSITEIMAGES = os.getenv(POKEMONWEBSITEIMAGES)
url = f"https://{POKEMONWEBSITEIMAGES}/Silver-Lance-Expansion/"]
r = requests.get(url)
html_content = BeautifulSoup(r.content, "html.parser")

cards = html_content.find_all("div", "card")

card_names = []

links_images = []


def get_images():
    print("Get Images: ")
    for card in cards:
        links_images.append(card.find("img")["data-src"])

    for i in range(len(links_images)):
        r = requests.get(links_images[i], stream=True)
        card_number = i + 1
        card_number = str(card_number)
        if ".jpg" in links_images[i]:
            title = card_number
            print("Downloading " + title + ".jpg")
            with open(title + ".jpg", "wb") as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        elif ".png" in links_images[i]:
            title = card_number
            print("Downloading " + title + ".png")
            with open(title + ".png", "wb") as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)


def get_names():
    for i in range(len(cards)):
        imgNumber = i + 1
        card_names.append(
            {
                "name": cards[i].find("div", "plaque").text,
                "imgFile": str(imgNumber) + ".png",
            }
        )
    print(card_names)


# get_images()
# get_names()
