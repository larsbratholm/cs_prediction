import sys
import imp
import os

cheshift_init_path = '/home/lab/.pymol/startup/cheshift/__init__.py'
if cheshift_init_path == "":
    print "set cheshift_init_path" in sys.argv[0]
    quit()

if len(sys.argv) == 1:
    print "Run as pymol -cqr %s -- <pdb-file1> (<pdb-file2> ...)"
    quit()

cheshift = imp.load_source('cheshift',cheshift_init_path)

for i in sys.argv[1:]:
    basename = i.split("/")[-1].split(".")[0]
    cmd.load(i)
    cheshift.run()
    os.system("mv %s %s" %(basename + ".txt", sys.argv[1]+".cheshift"))
    cmd.delete(basename)
cmd.quit()
