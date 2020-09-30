import time
import re
import requests
from bs4 import BeautifulSoup


def get_soup(url):
    try:
        req = requests.get(url, verify=False) 
    except requests.exceptions.RequestException as e:
        return None
    soup = BeautifulSoup(req.text, "html.parser")
    return soup


def simple_parser(url, balise, attr_titre, attr_valeur):
    soup = get_soup(url)
    if soup is None:
        return None
    else:
        ret = [
            el.text.strip()
            for el in soup.find_all(balise, attrs={attr_titre: attr_valeur})
        ]
        return ret
