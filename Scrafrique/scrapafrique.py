import pprint
import scrappers
import pickle



parsers = {
    "Bénin": scrappers.benin,
    "Burkina": scrappers.burkina,
    "Burundi":scrappers.burundi,
    "Cameroun":scrappers.cameroun,
    "Niger": scrappers.niger,
    "Sénégal": scrappers.senegal,
}


list_AO = dict.fromkeys(parsers.keys())
for key, value in parsers.items():
    list_AO[key] = value()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(list_AO)
