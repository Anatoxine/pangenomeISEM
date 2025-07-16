input_file = "pggb_gd_chr1_odgi.gfa"

existing_segments= set()
fixed_lines = []

with open(input_file, 'r') as f:
    lines = f.readlines()

    # Récupération des segments valides
    for line in lines:
        if line.startswith('S'):
            seg_id = line.strip().split('\t')[1]
            existing_segments.add(seg_id)

    # Correction des chemins P
    for line in lines:
        if line.startswith('P'):
            fields = line.strip().split('\t')
            seq_id = fields[1]
            path_elems = fields[2].split(',')

            filtered_path = []

            for seg in path_elems:
                seg_id = seg[:-1] 
                if seg_id in existing_segments:
                    filtered_path.append(seg)

            new_line = f"P\t{seq_id}\t{','.join(filtered_path)}\t*\n"
            fixed_lines.append(new_line)

    with open(input_file, 'w') as f2:
        for line in lines:
            if not line.startswith('P'):
                f2.write(line)
        f2.writelines(fixed_lines)
