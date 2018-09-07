import json
import pandas as p

# Parse lines
with open("nrf") as f:
    c = f.readlines()
#c = [x.split("|") for x in c]

jsons=[];
clean=[]; #array of clean results

# edit as json
for line in c:
    # leave only lines starting with "{"
    if(line[0]=="{"):
        jsonline=line.split('}')[0] #split names and IPs
        ip=line.split('}')[1]

        jl=json.loads(jsonline+"}"); #sorry
        jsons.append(jl)

for jl in jsons:
    line=[]
    if (jl['myname']!=''):
        line.append(jl['myname']);
        #print("====");
        #print("Name: "+jl['myname']);
        #if (jl['email']!=''):
                #print("email: "+jl['email']);
        try:
            line.append(len(jl['name']));
            #print("List 1: "+str(len(jl['name']))+"/95");
            #print(jl['name']);
        except KeyError:
            print("No name");
        try:
            #print("List 2: "+str(len(jl['name2']))+"/95");
            #print(jl['name2']);
            line.append(len(jl['name2']));
        except KeyError:
            print("No name2");
        try:
            line.append(jl['ok_share']);
        except KeyError:
            line.append("share");

    clean.append(line);
print(clean);

# Now let's analyse the hell out of this data!
d=p.DataFrame(data=clean);
d.columns=["name", "nlist1", "nlist2", "share"];
#sum column
d['tot']=d.sum(axis=1)

print(d);

d['f4']=d['tot']*(400/8)
d['f2']=d['tot']*(240/8)
d['f6']=d['tot']*(600/8)
print(d.loc[d['share']=='share'][['name','f2','f4','f6']].dropna(0).round(2).sort_values('f6'));

