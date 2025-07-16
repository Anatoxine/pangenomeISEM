import re
import os

input_gfa = "data/gd.full.gfa"
out_dir = "paths_cactus" 

#permet de creer un dossier
os.makedirs(out_dir, exist_ok=True)

with open(input_gfa, "r") as file:
    for line in file:
        # on s'interesse uniquement au ligne W contenant le chemin de segment d'un individu
        if line.startswith("W"):
            # decoupe la ligne avec les tabulations comme separateur
            fields = line.strip().split("\t")

            # recuperation de l'id de la sequence et son chemin
            seq_id = fields[1]
            seq_path = fields[6]

            # parse le chemin avec son sens et le reformate avec juste l'id du segment et un signe + ou -
            segments = re.findall(r'([><])(\d+)', seq_path)
            format_segment_bandage = [f"{num}{'+' if orientation == '>' else '-'}" for orientation, num in segments]
            
            # on cree un fichier au nom de l'id de la sequence
            filename = f"{seq_id.lower()}.txt"
            filepath = os.path.join(out_dir, filename)

            # ecriture du chemin dans le nouveau fichier
            with open(filepath, "w") as file:
                file.write(",".join(format_segment_bandage) + "\n")


