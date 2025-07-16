
from collections import defaultdict

# Fonction pour recuperer le chemin traverse pour chaque individu d'entree
def getPathMinigraph(paf_file):
    paths = defaultdict(list)

    # ouvre le fichier PAF genere par Minigraph-Cactus
    with open(paf_file) as file:
        # pour chaque ligne du fichier: on recupere l'id de la sequence concernee,
        # le segment qu'elle traverse et dans quelle direction
        for line in file:
            fields = line.strip().split('\t')
            seq_id = fields[0]
            direction = fields[4] 
            segment_field = fields[5]  # ex: id=_MINIGRAPH_|s1
            segment_id = None
            if segment_field.startswith('id=_MINIGRAPH_|'):
                segment_id = segment_field.split('|')[1] # on recupere uniquement l'id du segment qui se trouve apres le caractere |
            else:
                segment_id = segment_field

            paths[seq_id].append(( segment_id, direction))
    return paths

#on entre le lien du fichier paf 
paf_path = "data/gd_sv.paf"
paths = getPathMinigraph(paf_path)

# On cree deux fichiers texte pour repertorier les chemins des individus :
# un pour Bandage et un pour GfaViz

with open("bandage_ver.txt", "w") as file:
    for seq_id, values in paths.items():
        file.write(f">{seq_id}\n")          
        file.write(','.join(f"{seg_id}{dir_}" for seg_id, dir_ in values)+ "\n")


with open("gfaviz_ver.txt", "w") as file:
    for seq_id, values in paths.items():
        file.write(f">{seq_id}\n")          
        file.write(' '.join(f"{seg_id}" for seg_id, dir_ in values)+ "\n")