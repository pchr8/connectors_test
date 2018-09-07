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
for i in reversed(range(0, len(names))):
    for j in range (0, i):
        wnames.append(names[len(names)-i]);
ri=set(random.sample(wnames, 100));
ri2=set(random.sample(wnames, 100));

print("First list:")
print(ri);
print("Second list:")
print(ri2);

# And now we generate a php form out of it
html='';
i=1;
for n in ri:
    html+="<label for=\""+n+"\"> "+str(i)+": "+n+"</label>\n\n"
    html+="<input type=\"checkbox\" id=\""+n+"\" name=\"name\" value=\""+n+"\">\n" 
    i=i+1;
html+="\n=====================================\n";
i=1;
for n in ri2:
    html+="<label for=\""+n+"\"> "+str(i)+": "+n+"</label>\n\n"
    html+="<input type=\"checkbox\" id=\""+n+"\" name=\"name\" value=\""+n+"\">\n" i=i+1; 
htmlfile = open("form.html", "w", encoding='utf-8');
htmlfile.write(html);
htmlfile.close();
