import googlemaps
from tqdm import tqdm
from itertools import permutations
import mysql.connector
from collections import Counter

API_KEY="your api key"     #defining my api key
gmaps=googlemaps.Client(key=API_KEY) 
#make request to google through our client and key for authentication 
# places api documentation link "https://developers.google.com/places/web-service/intro"


#For 4 people with different drops
def droping(ab,fin,drop):       #fin will be the final list having all the matches found of 4
    bc=[]
    for i in ab:
        for j in ab:
            for k in ab:
                for l in ab:
                    a={i,j,k,l}
                    if(len(a)==4):
                        bc.append(a)
    abc=set(frozenset(x) for x in bc)

    li=[]     #isme each 4 ke set ke sare combinations ek ek list bn kr append honge 
    for y in abc:
        li.append(list(permutations(set(y))))
    lis=[]    #merging all in a same list
    for i in li:
        lis=lis+i
    liss=[]      #set to list
    for i in lis:
        liss.append(list(i))
    lis=liss
    #print(lis)
    fg=[]
    #print("huhh")
    for i in tqdm(lis):
        s=0.0
        #print(s)
        for p in range(3):
            jk=gmaps.distance_matrix(i[p][0],i[p+1][0])
            jkl=jk['rows'][0]['elements'][0]['distance']['text']
            s+=float(jkl.split()[0])
        jkbu=gmaps.distance_matrix(i[0][0],drop)
        jklbu=jkbu['rows'][0]['elements'][0]['distance']['text']
        s+=float(jklbu.split()[0])
        fg.append(s)
    lis[fg.index(min(fg))]
    py=lis[fg.index(min(fg))]
    fin.append(py)
    #print(py)
    for m in py:
        for l in ab:
            if(m==l):
                ab.remove(l)
    if(len(ab)<4):
        return ab,fin
    picking(ab,fin)




#For 2 people with same drop and 2 else with different pickups
def droping222(ab,lm,drop):    #ab is list with all single ones and lm is the same location of 2
    bc=[]
    for i in ab:
        for j in ab:
            a={i,j,lm}
            if(len(a)==3):
                bc.append(a)
    abc=set(frozenset(x) for x in bc)

    li=[]
    for y in abc:
        li.append(list(permutations(set(y))))
    lis=[]    #merging all in a same list
    for i in li:
        lis=lis+i
    liss=[]      #set to list
    for i in lis:
        liss.append(list(i))
    lis=liss
    fg=[]
    for i in lis:
        s=0.0
        for p in range(2):
            jk=gmaps.distance_matrix(i[p][0],i[p+1][0])
            jkl=jk['rows'][0]['elements'][0]['distance']['text']
            s+=float(jkl.split()[0])
        jkbu=gmaps.distance_matrix(i[2][0],drop)
        jklbu=jkbu['rows'][0]['elements'][0]['distance']['text']
        s+=float(jklbu.split()[0])
        fg.append(s)
    lis[fg.index(min(fg))]
    py=lis[fg.index(min(fg))]
    #print(py)
    for m in py:
        for l in ab:
            if(m==l):
                ab.remove(l)
    return ab,py



#For 3 people with same drop and 1 else with different pickups
def droping333(ab,lm,drop):    #ab is list with all single ones and lm is the same location of 3
    bc=[]
    for i in ab:
        a={i,lm}
        if(len(a)==2):
            bc.append(a)
    abc=set(frozenset(x) for x in bc)

    li=[]
    for y in abc:
        li.append(list(permutations(set(y))))
    lis=[]    #merging all in a same list
    for i in li:
        lis=lis+i
    liss=[]      #set to list
    for i in lis:
        liss.append(list(i))
    lis=liss
    fg=[]
    for i in lis:
        s=0.0
        for p in range(1):
            jk=gmaps.distance_matrix(i[p][0],i[p+1][0])
            jkl=jk['rows'][0]['elements'][0]['distance']['text']
            s+=float(jkl.split()[0])
        jkbu=gmaps.distance_matrix(i[1][0],drop)
        jklbu=jkbu['rows'][0]['elements'][0]['distance']['text']
        s=float(jklbu.split()[0])
        fg.append(s)
    lis[fg.index(min(fg))]
    py=lis[fg.index(min(fg))]
    #print(py)
    for m in py:
        for l in ab:
            if(m==l):
                ab.remove(l)
    return ab,py



#For 4 people with different drops
def picking(ab,fin,pick):       #fin will be the final list having all the matches found of 4
    bc=[]
    for i in ab:
        for j in ab:
            for k in ab:
                for l in ab:
                    a={i,j,k,l}
                    if(len(a)==4):
                        bc.append(a)
    abc=set(frozenset(x) for x in bc)

    li=[]     #isme each 4 ke set ke sare combinations ek ek list bn kr append honge 
    for y in abc:
        li.append(list(permutations(set(y))))
    lis=[]    #merging all in a same list
    for i in li:
        lis=lis+i
    liss=[]      #set to list
    for i in lis:
        liss.append(list(i))
    lis=liss
    #print(lis)
    fg=[]
    #print("huhh")
    for i in tqdm(lis):
        jkbu=gmaps.distance_matrix(pick,i[0][0])
        jklbu=jkbu['rows'][0]['elements'][0]['distance']['text']
        s=float(jklbu.split()[0])
        #print(s)
        for p in range(3):
            jk=gmaps.distance_matrix(i[p][0],i[p+1][0])
            jkl=jk['rows'][0]['elements'][0]['distance']['text']
            s+=float(jkl.split()[0])
        fg.append(s)
    lis[fg.index(min(fg))]
    py=lis[fg.index(min(fg))]
    fin.append(py)
    #print(py)
    for m in py:
        for l in ab:
            if(m==l):
                ab.remove(l)
    if(len(ab)<4):
        return ab,fin
    picking(ab,fin)


#For 2 people with same drop and 2 else with different pickups
def picking222(ab,lm,pick):    #ab is list with all single ones and lm is the same location of 2
    bc=[]
    for i in ab:
        for j in ab:
            a={i,j,lm}
            if(len(a)==3):
                bc.append(a)
    abc=set(frozenset(x) for x in bc)

    li=[]
    for y in abc:
        li.append(list(permutations(set(y))))
    lis=[]    #merging all in a same list
    for i in li:
        lis=lis+i
    liss=[]      #set to list
    for i in lis:
        liss.append(list(i))
    lis=liss
    fg=[]
    for i in lis:
        jkbu=gmaps.distance_matrix(pick,i[0][0])
        jklbu=jkbu['rows'][0]['elements'][0]['distance']['text']
        s=float(jklbu.split()[0])
        for p in range(2):
            jk=gmaps.distance_matrix(i[p][0],i[p+1][0])
            jkl=jk['rows'][0]['elements'][0]['distance']['text']
            s+=float(jkl.split()[0])
        fg.append(s)
    lis[fg.index(min(fg))]
    py=lis[fg.index(min(fg))]
    print(py)
    for m in py:
        for l in ab:
            if(m==l):
                ab.remove(l)
    return ab,py


#For 3 people with same drop and 1 else with different pickups
def picking333(ab,lm,pick):    #ab is list with all single ones and lm is the same location of 3
    bc=[]
    for i in ab:
        a={i,lm}
        if(len(a)==2):
            bc.append(a)
    abc=set(frozenset(x) for x in bc)

    li=[]
    for y in abc:
        li.append(list(permutations(set(y))))
    lis=[]    #merging all in a same list
    for i in li:
        lis=lis+i
    liss=[]      #set to list
    for i in lis:
        liss.append(list(i))
    lis=liss
    fg=[]
    for i in lis:
        jkbu=gmaps.distance_matrix(pick,i[0][0])
        jklbu=jkbu['rows'][0]['elements'][0]['distance']['text']
        s=float(jklbu.split()[0])
        for p in range(1):
            jk=gmaps.distance_matrix(i[p][0],i[p+1][0])
            jkl=jk['rows'][0]['elements'][0]['distance']['text']
            s+=float(jkl.split()[0])
        fg.append(s)
    lis[fg.index(min(fg))]
    py=lis[fg.index(min(fg))]
    #print(py)
    for m in py:
        for l in ab:
            if(m==l):
                ab.remove(l)
    return ab,py


