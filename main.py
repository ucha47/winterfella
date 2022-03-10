import requests
import json

r = requests.get('http://api.citybik.es/v2/networks')

jsontext = r.text

#print(jsontext)

events = r.json()

#print(events)

#if 'Fr' in jsontext:
#    print("True")
#else:
#    print("False")





text_json = json.loads(r.text)
print(text_json['name'])





