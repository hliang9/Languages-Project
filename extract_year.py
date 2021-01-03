import os
from pathlib import Path
import re

DIRECTORY = 'xml'
for root, _, files in os.walk(directory):
    for file in files:
        if not file.endswith('.xml'):
            continue
        f_name = (os.path.join(root, file))
        with open(f_name, 'r') as f:
            line = f.readline()
            while line and '<date>' not in line: 
                line = f.readline() 
            searcher = re.search('(?<=<date>)[0-9]+(?=.*<\/date>)', line) # match the first date that occurs between the tags <date> </date>
            if not searcher:
                print(f_name)
            year = searcher.group(0)
            century = year[:2] + "00"
            path = os.path.join('date_txt', century)
            os.makedirs(path, exist_ok = True) 
        with open(os.path.join(path, Path(file).stem + ".txt"), 'w') as f:
            f.write(year)