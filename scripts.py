import numpy as np

def Levenshtein_Analysis(string1, string2):
    dist = np.zeros((len(string1) + 1, len(string2) + 1))

    for t1 in range(len(string1) + 1):
        dist[t1][0] = t1

    for t2 in range(len(string2) + 1):
        dist[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(string1) + 1):
        for t2 in range(1, len(string2) + 1):
            if (string1[t1-1] == string2[t2-1]):
                dist[t1][t2] = dist[t1 - 1][t2 - 1]
            else:
                a = dist[t1][t2 - 1]
                b = dist[t1 - 1][t2]
                c = dist[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    dist[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    dist[t1][t2] = b + 1
                else:
                    dist[t1][t2] = c + 1

    return dist[len(string1)][len(string2)]