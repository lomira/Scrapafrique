import time

import requests
from bs4 import BeautifulSoup


def get_soup(url):
    try:
        req = requests.get(url)
    except requests.exceptions.RequestException as e:
        return None
    soup = BeautifulSoup(req.text, "html.parser")
    return soup


def niger(url):
    soup = get_soup(url)
    if soup is None:
        return None
    else:
        h4list = [h4.text.strip() for h4 in soup.find_all("h4", attrs={"class": None})]
        return h4list


def senegal(url):
    soup = get_soup(url)
    if soup is None:
        return None
    else:
        divlist = [
            div.text.strip()
            for div in soup.find_all(
                "div", attrs={"class": "views-field views-field-title"}
            )
        ]
        return divlist