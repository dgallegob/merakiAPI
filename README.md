# merakiAPI
- Script that interacts with Cisco Meraki Rest API <br/>
- Written in Python and it uses requests library to perform HTTP requests. <br/>
- usingMErakiApi.py to be executed and it imports danmerakiapi.py <br/
- Don't forget to modify the first line of the code to add the location of the python interpreter on your machine <br/
- Required libraries: requests, json, argparse, webbrowser <br/>
- --key parameter is required to run the script (API Key) <br/>
- It currently support the below functionalities: <br/>
1) List the organizations that the user has privileges on <br/>
2) List all networks of all (or single) organizations. <br/>
3) Given a SN, it finds the organization the SN belongs to.

