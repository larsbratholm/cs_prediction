import sys

lines = open(sys.argv[1]).readlines()
pdb = open(sys.argv[2]).readlines()

pdb_info = {}
for line in pdb:
    if "ATOM" not in line:
        continue
    tokens = line.split()

    res_no = int(tokens[5])
    res_type = tokens[3]
    atom_name = tokens[2]
    atom_type = atom_name[0]
    if res_no not in pdb_info: pdb_info[res_no] = {}
    pdb_info[res_no][atom_name] = [res_no,res_type,atom_name,atom_type]


atom_type = None
ca_list = []
cb_list = []
for line in lines:
    tokens = line.split()
    if len(tokens) == 0:
        continue
    if tokens[0] == "Ca":
        atom_type = "CA"
        continue
    elif tokens[0] == "Cb":
        atom_type = "CB"
        continue
    res_type = tokens[0]
    cs = tokens[1]
    if atom_type == "CA":
        ca_list.append([res_type, cs])
    else:
        cb_list.append([res_type, cs])

# stupid simple criteria
if (len(pdb_info.keys()) != len(ca_list)) and min(pdb_info.keys) != 1:
    print "len error"
    quit()


count = 1
for i in sorted(pdb_info.keys()):
    pdb_ca = pdb_info[i]["CA"]
    cs_ca = ca_list[i-1]

    if pdb_ca[1] != cs_ca[0]:
        print "residue mismatch"
        print pdb_ca, cs_ca
        quit()

    if cs_ca[1] != "999.00":
        print count, i, pdb_ca[1], pdb_ca[2], pdb_ca[3], cs_ca[1]
        count += 1


    if "CB" in pdb_info[i]: pdb_cb = pdb_info[i]["CB"]
    else: continue
    cs_cb = cb_list[i-1]

    if pdb_cb[1] != cs_cb[0]:
        print "residue mismatch"
        print pdb_cb, cs_cb
        quit()

    
    if cs_cb[1] != "999.00":
        print count, i, pdb_cb[1], pdb_cb[2], pdb_cb[3], cs_cb[1]
        count += 1



