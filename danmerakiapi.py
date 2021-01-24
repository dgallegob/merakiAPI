#!/usr/bin/python3.5
import requests
import json


basic_url='https://dashboard.meraki.com/api/v1/'

def find_slash (url) :
	url=url[0:(url.rfind('/'))+1]
	url=url+'inventory'
	return (url)

def find_orgs (api_key):
	headers = {
		'X-Cisco-Meraki-API-Key': api_key,
		'Content-Type': 'application/json',
	}
	url=basic_url+'organizations'
	return (requests.get(url, headers=headers)).json()
	
def find_networks (api_key):
	headers = {
		'X-Cisco-Meraki-API-Key': api_key,
		'Content-Type': 'application/json',
	}
	orgs=find_orgs(api_key)
	array=[]
	j=0
	for i in range(len(orgs)):
		id=orgs[i]['id']
		name=orgs[i]['name']
		url=basic_url+'organizations/'+id+'/networks'
		response=requests.get(url, headers=headers)
		status=response.status_code
		if status == 404 :
			print ("Organization"+str(i+1),id,name,"-> API disabled")
		else:
			data=response.json()
			array.append(data)
			print ("Organization"+str(i+1),id,name,"-> API enabled")
	return (array)

def find_device (api_key,sn):
	headers = {
		'X-Cisco-Meraki-API-Key': api_key,
		'Content-Type': 'application/json',
	}
	data=find_orgs(api_key)
	for i in range(len(data)):
		id=data[i]['id']
		name=data[i]['name']
		url=basic_url+'organizations/'+id+'/inventoryDevices'
		response=requests.get(url, headers=headers)
		status=response.status_code
		if status == 404:
			print ("Organization",i+1,id,"hasn't enabled API")
		else:
			data2=response.json()
			for j in range(len(data2)):
				if str(data2[j]['serial']) == sn:
					url=find_slash(data[i]['url'])
					return (sn+' belongs to the org '+(data[i]['id'])+' '+data[i]['name']+' '+(data[i]['url']),url)


