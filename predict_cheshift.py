import sys
import imp
import inspect, os
from contextlib import contextmanager

# from http://thesmithfam.org/blog/2012/10/25/temporarily-suppress-console-output-in-python/#
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout


scriptpath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

cheshift_init_path = '/home/lab/.pymol/startup/cheshift/__init__.py'
if cheshift_init_path == "":
    print "set cheshift_init_path" in sys.argv[0]
    quit()

if len(sys.argv) == 1:
    print "Run as pymol -cqr %s -- <pdb-file1> (<pdb-file2> ...)"
    quit()

cheshift = imp.load_source('cheshift',cheshift_init_path)


for pdb in sys.argv[1:]:
    basename = pdb.split("/")[-1].split(".")[0]
    with suppress_stdout():
        cmd.load(pdb)
        cheshift.run()
    os.system("python2 %s %s %s " %(scriptpath+"/cheshift_to_star.py", basename + ".txt", pdb))
    cmd.delete(basename)
    os.system("rm %s" % basename + ".txt")
cmd.quit()
