import sys

pdb = open(sys.argv[1]).readlines()

pdb_info = {}
for line in pdb:
    if line.startswith("ATOM") == False:
        continue
    tokens = line.split()

    # if no chain name is given, then the res number will be in column 5
    try:
        res_no = int(tokens[5])
    except ValueError:
        res_no = int(tokens[4])
    res_type = tokens[3]
    atom_name = tokens[2]
    atom_type = atom_name[0]
    if res_type == "GLY" and atom_name == "HA3":
        atom_name = "HA"
    if res_no not in pdb_info: pdb_info[res_no] = {}
    pdb_info[res_no][atom_name] = [res_no,res_type,atom_name,atom_type]


flag = False
cs_list = {}
for name in ["HA","CA","H","N","C","CB"]:
    cs_list[name] = []


for line in sys.stdin.readlines():
    if line.startswith("-----"):
        flag = True
        continue
    elif flag == False:
        continue

    tokens = line.split()

    res_type = tokens[1]
    for n, name in enumerate(["HA","CA","H","N","C","CB"]):
        cs = tokens[n+2]
        cs_list[name].append([res_type,cs])

# stupid simple criteria
if (len(pdb_info.keys()) != len(cs_list["CA"])) and min(pdb_info.keys()) != 1:
    print "len error"
    quit()


count = 1
for i in sorted(pdb_info.keys()):
    for n in ["HA","CA","H","N","C","CB"]:
        if n in pdb_info[i]: pdb = pdb_info[i][n]
        else: continue
        cs = cs_list[n][i-1]

        if pdb[1] != cs[0]:
            print "residue mismatch"
            print pdb, cs
            quit()

        if cs[1] != "0.0000":
            print count, i, pdb[1], pdb[2], pdb[3], cs[1]
            count += 1
