import requests

resp = requests.get('https://pyearn.herokuapp.com/api')
resp = resp.json()

roi = resp['crv']
print(roi)