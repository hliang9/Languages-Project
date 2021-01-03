import regex, sys
from glob import glob
import os 

directory = 'balanced_txt/'
token_pattern = regex.compile("(\w[\w\'\-]*\w|\w)")
for f_name in glob(directory + "**/*.txt"):
    with open(f_name, 'r') as reader:
        os.makedirs('no_punct', exist_ok = True) 
        with open(os.path.join('no_punct', os.path.basename(f_name)), 'a+') as writer: 
            for line in reader: 
                line = line.lower().replace("∣", "")
                tokens = token_pattern.findall(line)
                writer.write(" ".join(tokens) + "\n")
