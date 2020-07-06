import os, glob
files = glob.glob('pw_lists/*.txt')

all_lines = []
for f in files:
    with open(f,'r') as fi:
        all_lines += fi.readlines()

all_lines = set(all_lines)

with open('pwds.txt','w') as fo:
    fo.write("".join(all_lines))