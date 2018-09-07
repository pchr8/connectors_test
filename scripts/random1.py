import random

# Parse lines
with open("ukrnames") as f:
    c = f.readlines()
c = [x.split("|") for x in c]

names=[]; #names from list
wnames=[]; #a representative sample

# Clear names
for line in c:
    names.append(line[1].strip());

# Now we pick them pseudorandomly, favouring the names at the beginning of the list 
# https://stackoverflow.com/questions/14992521/python-weighted-random

# Names which are closer to the beginning will appear more often
ri=set(random.sample(names, 100));

print("First list:")
print(ri);
