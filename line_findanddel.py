import re
 
with open(del_file, "r+") as f:
    p = re.compile("0.000|aol|1.000")
    lines = [line for line in f.readlines() if p.search(line) is None]
    f.seek(0)
    f.truncate(0)
    f.writelines(lines)


del_file = "1.txt"
