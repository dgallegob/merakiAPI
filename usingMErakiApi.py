#!/usr/bin/python3.5
import json
import argparse
import webbrowser
import danmerakiapi


#Parsing arguments, API key is required
parser = argparse.ArgumentParser()
parser.add_argument('--key' , dest='apiKey' , required = True, help='API key')
args = parser.parse_args()
apiKey = args.apiKey



action = 0

#Selection action
while not action in [ 1,2,3]:
	print ("Please type 1, 2 or 3 to select which action you would like to perform")
	action=int(input("1 (list orgs), 2 (list networks), 3 (find device)\n"))

print("Action selected: ", action)

#Action 1: list all orgs the user is part of
if int(action) == 1:
	orgs=danmerakiapi.find_orgs(apiKey)
	print("You are part of the following orgs\nID 	NAME 	URL")	
	for i in range(len(orgs)):
		id=orgs[i]['id']
		name=orgs[i]['name']
		url=orgs[i]['url']
		print (id,name,url)

#Action 2: List networks
elif int(action) == 2:
	array_networks_orgs = danmerakiapi.find_networks(apiKey)
	action = 0
	while not action in [1,2]: 
		action=int(input("Do you want to check all orgs/networks (1), one specific org (2)\n"))
#We can list all networks of all orgs
	if int(action)==1:
		for i in range(len(array_networks_orgs)):
                    current_org = array_networks_orgs[i]
                    org_id = current_org[0]['organizationId']
                    print("Organization ID %s" % org_id)
                    for j in range(len(current_org)):
                    	print ("Network"+str(j+1),current_org[j]['id'],current_org[j]['name'],current_org[j]['productTypes'])
#Or we can list the networks of 1 specific org
	elif int(action) == 2:
		for i in range (len(array_networks_orgs)):
			print(array_networks_orgs[i][0]['organizationId'])
		orgid=input("Which org do you want check?\n")
		for i in range (len(array_networks_orgs)):
			current_org = array_networks_orgs[i]
			if orgid == current_org[0]['organizationId']:
				for j in range(len(current_org)):
					print ("Network"+str(j+1),current_org[j]['id'],current_org[j]['name'],current_org[j]['productTypes'])



#Given a SN, it search for that SN in all orgs and open a the browser with the link of the org if the SN is found                     
elif int(action) == 3:
	sn=input("Provide SN\n")
	device_info = danmerakiapi.find_device(apiKey,sn)
	if device_info:
		print (device_info[0])
		webbrowser.open_new(device_info[1])
	else:
		print(sn,"does not belong to any of the orgs you have access to, wrong SN or you need to enable API on the org")




	
		
	

 
