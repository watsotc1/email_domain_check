import json
from scripts import Levenshtein_Analysis

#load in trusted domains
fid = open('trusted_domains.json',)
data = json.load(fid)
trusted_domains = data['trusted_domains']
fid.close()

#load in domains to be checked
fid = open('domains_to_test.json',)
data = json.load(fid)
domains_to_test = data['domains_to_test']
fid.close()

# Set Tolerance
tol = 5
for i in domains_to_test:
    #reset current for each domain
    curr = 1e3
    for j in trusted_domains:
        diff = Levenshtein_Analysis(i, j)
        
        #If domain matches better than last set as closest
        if diff < curr:
            curr = diff
            closest_domain = j
            
    #Classify Domain Threat Level
    if curr > tol:
        threat_level = 'Danger'
        text_color = 'red'
    else:
        threat_level = 'Risky'
        text_color = 'green'
    
    #Create/Print Output Data
    output = {
        'Domain': i,
        'Closest Trusted Domain': closest_domain,
        'Levenshtein Distance': curr,
        'Threat Level': threat_level
    }
    print(output)
        

