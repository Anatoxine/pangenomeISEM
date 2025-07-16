import gfapy

# renseignement des segments que l'on souhaite avoir
# dans le sous graphe
wanted = {"9441", "9442", "7807", "7806", "7805", "7804", "7801"}

# recuperation du gfa deja cree
gfa = gfapy.Gfa.from_file("data/pggb_gd_chr1_sub_sub_fixed.gfa")

# initialisation d'un nouveau graphe
subgraph = gfapy.Gfa()

#on copie chaque segment voulu dans le nouveau graphe
for segment in gfa.segments:
    if segment.name in wanted:
        subgraph.add_line(segment.clone()) 

# on recupere les liens entre les segments recuperes
for link in gfa.edges:
    from_seg = link.from_segment.name
    to_seg = link.to_segment.name

    if from_seg in wanted and to_seg in wanted:
        subgraph.add_line(link.clone()) 


# on enregistre ce nouveau graphe au format gfa
subgraph.to_file("pggb_gd_chr1_sub_sub_sub.gfa")





