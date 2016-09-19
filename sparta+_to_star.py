import sys

aa1="AcCDEFGHIKLMNPQRSTVWY"
aa3=["ALA", "CYS", "CYS", "ASP", "GLU", "PHE", "GLY", "HIS", "ILE", "LYS", "LEU",
     "MET", "ASN", "PRO", "GLN", "ARG", "SER", "THR", "VAL", "TRP", "TYR"]


res_3to1 = {}
for i in range(0, 21):
    res_3to1[aa3[i]] = aa1[i]

res_1to3 = {}
for i in range(0, 21):
    res_1to3[aa1[i]] = aa3[i]


lines = open(sys.argv[1]).readlines()

flag = False


count = 1
for line in lines:
    if "FORMAT" in line:
        flag = True
        continue
    elif flag == False:
        continue
    if len(line) < 2:
        continue

    tokens = line.split()
    if tokens[2] == "HN":
        tokens[2] = "H"
    print count, tokens[0], res_1to3[tokens[1]], tokens[2], tokens[2][0], tokens[4]
    count += 1
