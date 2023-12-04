import re

text = "twoneight"

for x in re.findall(r'(?=(one|two|eight))',text):
    print (" - ",x)