import requests
import json

req = requests.get('https://api.warframestat.us/pc/cetusCycle')
def jprint(obj):
    text = json.dumps(obj, sort_keys = True, indent = 4)
    print(text)
timeleft = req.json()['timeLeft']
jprint(timeleft)