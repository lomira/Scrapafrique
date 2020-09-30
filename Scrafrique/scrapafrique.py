import pprint
import re
import scrappers
import pickle


config = {
    "Bénin": ["https://arcep.bj/communiques/", "td", "class", "column-2"],
    "Burkina": [
        "http://www.arcep.bf/category/actualites/",
        "h4",
        "class",
        "pl-title left-txt",
    ],
    "Burundi": [
        "http://arct.gov.bi/index.php/publications/travaux-de-recherche",
        "p",
        "style",
        "text-align: justify;",
    ],
    "Cameroun": [
        "http://www.art.cm/fr/reglementation/dao",
        "div",
        "class",
        "views-row-inner",
    ],
    "Centrafrique": [
        "https://www.arcep.cf/index.php/actualites/communiques",
        "div",
        "class",
        "kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q",
    ],
    "Comores": [
        "https://www.anrtic.km/publication/appel-d-offre.html",
        "h4",
        "class",
        "list-group-item-heading",
    ],
    "Congo": [
        "https://www.arpce.cg/avis",
        "h3",
        "class",
        "head",
    ],
    "RDC": [
        "https://www.arptc.gouv.cd/publications/appels-doffres",
        "",
        "",
        "",
    ],
    "Côte d'Ivoire": [
        "https://www.artci.ci/index.php/consultations-publiques/",
        "h1",
        "",
        "",
    ],
    "Gabon": [
        "https://www.arcep.ga/PASDAO",
        "",
        "",
        "",
    ],
    "Guinée": [
        "https://www.arpt.gov.gn/redaction/appels-d-offres",
        "div",
        "class",
        "field_date_create_article",
    ],
    "Madagascar": ["http://www.artec.mg/offres.php?id=2", "h4", "class", "heading"],
    "Mali": [
        "https://www.amrtp.ml/",
        "div",
        "class",
        re.compile("^aidanews2_art aidacat_87"),
    ],
    "Maroc": ["https://www.anrt.ma/publications/appels-doffres/consulter-les-appels-doffres", "span", "class", "field-content"],
    "Maurice": ["https://www.icta.mu/mediaoffice/tender.htm", "li", "", ""],
    "Mauritanie": ["http://are.mr/index.php/avis-et-communiques", "h2", "class", "article-title"],
    "Niger": ["https://www.arcep.ne/publications.php?sid=96", "h4", "class", None],
    "Sénégal": [
        "https://www.artpsenegal.net/fr/espace-pro/appels-doffres",
        "li",
        "class",
        re.compile("row-ao$"),
    ],
    "Tchad": ["https://arcep.td/avis", "span", "class", "avis-title"],
    "Togo": ["http://www.artp.tg/", "p", "id", "p_titre"],
    "Tunisie": ["http://www.intt.tn/fr/index.php?allao", "span", "class", "dateactu"]
}

list_AO = dict.fromkeys(config.keys())
for key, value in config.items():
    list_AO[key] = scrappers.simple_parser(value[0], value[1], value[2], value[3])

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(list_AO)
