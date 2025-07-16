import os

# ce script fonctionne uniquement avec les fichiers GFA générés par PGGB, qui contiennent des lignes P (path)


# nom du fichier entrant
gfa_file = "data/pggb_gd_chr1_sub_sub_fixed.gfa" 
sub = True

# creation du dossier de sortie contenant les resultats
output_dir = "gd_chr1_inversion_gfaviz" 
os.makedirs(output_dir, exist_ok=True)

if(sub):
    existing_segments = set()
    with open(gfa_file, 'r') as file:
        for line in file:
            if line.startswith("S"):
                parts = line.strip().split('\t')
                segment_id = parts[1]  
                existing_segments.add(segment_id)

with open(gfa_file, 'r') as file:
    for line in file:

        # on ne s'interesse qu'aux lignes P, contenant les chemins des individus
        if line.startswith("P"):
            # decoupage la ligne en fonction des tabulations
            parts = line.strip().split('\t')

            # recuperation de l'identifiant de l'individu et des identifiants des segments
            individual_id = parts[1] 
            segment_part = parts[2].split(',')
            if(sub):
                segment_part  = [seg for seg in segment_part if seg[:-1] in existing_segments]        


            # creation d'une liste pour les segments concernés par une inversion (-)
            inversions = [seg[:-1] for seg in segment_part if seg.endswith('-')]

            #creation d'une liste pour tous les segments 
            segments = [seg[:-1] for seg in segment_part ]

            #creation d'un fichier txt contenant les segments inversés d'un individu
            inversion_path = os.path.join(output_dir, f"{individual_id}_inversions.txt")
            with open(inversion_path, 'w') as out_file:
                out_file.write(' '.join(inversions))

            #creation d'un fichier txt contenant tous les segments traversés par un individu
            all_path = os.path.join(output_dir, f"{individual_id}_path.txt")
            with open(all_path, 'w') as out_file:
                out_file.write(' '.join(segments))
