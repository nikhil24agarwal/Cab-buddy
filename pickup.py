from functions import picking,picking333,picking222
import googlemaps
from tqdm import tqdm
from itertools import permutations
import mysql.connector
from collections import Counter
from flask_mail import Mail, Message
import app
from mail import maill
from flask import Flask

API_KEY="your api key"     #defining my api key
gmaps=googlemaps.Client(key=API_KEY) 
#make request to google through our client and key for authentication 
# places api documentation link "https://developers.google.com/places/web-service/intro"





def pickup_function():

	pickupp =Flask(__name__)

	mail=Mail(pickupp)
	pickupp.config['MAIL_SERVER']='smtp.gmail.com'
	pickupp.config['MAIL_PORT'] = 465
	pickupp.config['MAIL_USERNAME'] = 'easycabpooling@gmail.com'
	pickupp.config['MAIL_PASSWORD'] = '9928027274'
	pickupp.config['MAIL_USE_TLS'] = False
	pickupp.config['MAIL_USE_SSL'] = True
	mail = Mail(pickupp)


	ab = mysql.connector.connect(host="localhost",user="root",password="Sweta@12386",
                            db="data")
	cur = ab.cursor()
	cur.execute("Select drop_location,email from pickup")
	r=cur.fetchall()
	#print(r)

	lo_st = []
	loc_list=[]

	for i in r:
	    lo_st.append(list(i))
	for j in lo_st:
	    place = j[0]
	    place_auto = gmaps.places_autocomplete(place)
	    if(len(place_auto)==0):
	        pass        
	    else:
	        j[0] = place_auto[0]['description']

	for i in lo_st:
	    loc_list.append(tuple(i))


	final=[]       #final list with all matches
	pick ='bennett university, greater noida'     #pickup for all is fixed that is Bennett University

	#frequency of each location using counter library
	location_list=[]
	for i in loc_list:
	    location_list.append(i[0])

	counter=dict(Counter(location_list))       #dict bna di jisme key is location nd value is frequency

	freq_list=[]
	for j in counter.items():                  #dictionary se list
	    freq_list.append(list(j))
	    
	#4 entries with same drop are matched
	mm=loc_list[:]
	for k in freq_list:
	    n=int(k[1]/4)        #checking 4 ke kitte multiples mein hai same location
	    if(n>0):        #agr 4 ya jada same hai to delete krna hai nd return krna hai
	        for j in range(n):   #loop ko 4 ke lie 1 baar, 8 ke liye 2 baar ase chalana hai
	            k[1]=k[1]-4      #freq-4
	            m=0              #counter ki 4 delete huye ek baar mein
	            mn=[]            #to store all 4 entries jo ek saath match huyi
	            l=0              #list mein traverse and access krne ke liye 
	            cou=0
	            while cou<len(mm):     
	                #print(mm[l],m)
	                if(mm[l][0]==k[0]):
	                    mn.append(mm[l])
	                    mm.remove(mm[l])
	                    m+=1
	                    if(m==4):       #ek sath ke 4 hote hi bahar niklo loop se
	                        break
	                else:
	                    cou+=1
	                    l+=1
	            final.append(mn)
	            #print(mn)   #in sab ke pass match found bhej do and sql table se remove krdo in values ko

	#new frequencies

	#print(final)

	locst=[]
	for i in mm:
	    locst.append(i[0])

	counter=dict(Counter(locst))       #dict bna di jisme key is location nd value is frequency

	# 3,2 and 1 frequency valo ko separate kro
	li3=[]
	li2=[]
	li1=[]
	for i in mm:
	    if(counter[i[0]]==1):
	        li1.append(i)
	    elif(counter[i[0]]==2):
	        li2.append(i)
	    elif(counter[i[0]]==3):
	        li3.append(i)


	#print("b")


	nn3=int(len(li3)/3)
	for i in range(nn3):
	    v=[]
	    print("c")
	    if(len(li1)>0):
	        demo_final=[]
	        try3 = picking333(li1,li3[3*i],pick)
	        li1 = try3[0]
	        v = try3[1]
	    else:
	        v.append(li3[3*i])
	    v.append(li3[3*i+1])
	    v.append(li3[3*i+2])
	    final.append(v)
	    #li3.remove()
	#print(final)

	nn2=int(len(li2)/2)

	for i in range(nn2):
	    v=[]
	   # print("d")
	    if(len(li1)>1):
	        try2 = picking222(li1,li2[2*i],pick)
	        li1 = try2[0]
	        v = try2[1]
	    elif(len(li1)==1):
	        try2 = picking333(li1,li2[2*i],pick)
	        li1 = try2[0]
	        v = try2[1]
	    else:
	        v.append(li2[2*i])
	    v.append(li2[2*i+1])
	    final.append(v)

	#print(final)
	        

	if(len(li1)>3):
	    try1 = picking(li1,final,pick)
	    li1 = try1[0]
	    final = try1[1]
	elif(len(li1)>0):
	    v=[]
	    for i in li1:
	        v.append(i)
	    final.append(v)

	
	print(final)

	for i in final:
		recp_list=[]
		recp_name=[]
		for j in i:
			recp_list.append(j[1])
			cur.execute("select username,phone_no from credentials where email = \"%s\";"%j[1])
			row = cur.fetchall()
			k =""
			l=""
			for items in row:
				k=items[0]
				l=items[1]
			recp_name.append("%s is going to %s and contact no is %s and mail id is %s"%(k,j[0],l,j[1]))
		space="              \n"
		space = space.join(recp_name)
		final_msg="The best match we could find is :  \n"+space
		print("listtttttttttt",recp_list)
		maill(recp_list,final_msg)
		# msg = Message('you found your partner', sender = 'easycabpooling@gmail.com', recipients = recp_list)
		# msg.body = final_msg
		# mail.send(msg)
		print("senttt")


	cur.execute("Truncate table pickup;")

	return final
