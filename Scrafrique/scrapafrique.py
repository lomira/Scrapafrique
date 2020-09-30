import scrappers
import helpers
import pickle

pickle_path = "data/output.pickel"
with open(pickle_path, "rb") as f:
    niger_old, senegal_old = pickle.load(f)

# niger_old = []
niger = scrappers.niger("https://www.arcep.ne/publications.php?sid=96")
nouveaux = set(niger) - set(niger_old)
if nouveaux:
    print(*nouveaux, sep="\n")


senegal = scrappers.senegal("https://www.artpsenegal.net/fr/espace-pro/appels-doffres")
# print(*senegal, sep="\n")


with open(pickle_path, "wb") as f:
    pickle.dump([niger, senegal], f)