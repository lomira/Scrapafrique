import time
import re
import grequests
import urllib3

from bs4 import BeautifulSoup

# Evite les warning parce qu'on évite les connection SSL pas sécurisées de certains sites
urllib3.disable_warnings()


def get_resp(dict_config: dict):
    """Renvoie les responses HTTPs d'une liste d'url

    Args:
        dict_config (dict): Pays:URL

    Returns:
        dict: Pays:HTTPResponses
    """
    urls = [value[0] for (key, value) in dict_config.items()]
    reqs = (grequests.get(u) for u in urls)
    resps = grequests.map(reqs)
    return dict(zip(dict_config.keys(), resps))


def simple_parser(soup, balise, attr_titre, attr_valeur):
    """Renvoie les élements de la balise avec attr_titre=attr_valeur depuis une Response HTTP
    Args:
        soupe : HTTPResponse
        balise : nom de la basise à parser
        attr_titre : attribut de la balise à parse (id, class, etc.)
        attr_valeur : valeur de l'attribu

    Returns:
        [list]: list des textes qui remplissent les conditions
    """
    if soup is None:
        return None
    else:
        soup = BeautifulSoup(soup.text, "html.parser")
        ret = [
            el.text.strip()
            for el in soup.find_all(balise, attrs={attr_titre: attr_valeur})
        ]
        return ret
