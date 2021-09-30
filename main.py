import json
from scripts import Levenshtein_Analysis

"""
(Option 2) Write a program that maintains a list of “trusted” domains and 
takes as input an arbitrarily-sized list of other domains and a number. 
The function will check each input domain and if the Levenshtein distance is 
below the input number, list the domain as risky along with the domain that 
it is similar to and the distance.
"""

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

tol = 5
for i in domains_to_test:
    #reset current for each domain
    curr = 1e3
    for j in trusted_domains:
        diff = Levenshtein_Analysis(i, j)

        if diff < curr:
            curr = diff
            closest_domain = j
    
    if curr > tol:
        threat_level = 'Danger'
        text_color = 'red'
    else:
        threat_level = 'Risky'
        text_color = 'green'

    output = {
        'Domain': i,
        'Closest Trusted Domain': closest_domain,
        'Levenshtein Distance': curr,
        'Threat Level': threat_level
    }
    print(output)
        

