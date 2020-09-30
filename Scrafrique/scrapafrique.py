import scrappers


niger = scrappers.niger("https://www.arcep.ne/publications.php?sid=96")
# print(*niger, sep="\n")


senegal = scrappers.senegal(
    "https://www.artpsenegal.net/fr/espace-pro/appels-doffres"
)
print(*senegal, sep="\n")