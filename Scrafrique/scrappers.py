import time
import re
import requests
from bs4 import BeautifulSoup


def get_soup(url):
    try:
        req = requests.get(url)
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


def benin():
    return simple_parser("https://arcep.bj/communiques/", "td", "class", "column-2")


def burkina():
    return simple_parser(
        "http://www.arcep.bf/category/actualites/", "h4", "class", "pl-title left-txt"
    )


def burundi():
    return simple_parser(
        "http://arct.gov.bi/index.php/publications/travaux-de-recherche",
        "p",
        "style",
        "text-align: justify;",
    )


def cameroun():
    return simple_parser(
        "http://www.art.cm/fr/reglementation/dao", "div", "class", "views-row-inner"
    )


def niger():
    return simple_parser(
        "https://www.arcep.ne/publications.php?sid=96", "h4", "class", None
    )

def senegal():
    return simple_parser(
        "https://www.artpsenegal.net/fr/espace-pro/appels-doffres", "li", "class", re.compile("row-ao$")
    )
