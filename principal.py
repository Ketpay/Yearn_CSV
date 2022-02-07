import requests

from datetime import datetime
import csv
import time

crytos=["MIM", "DAI", "USDT", "USDC"]
csv_file=[["Nombre","Activos Totales","APY","Fecha"]]
i=True

file= open('data.csv', 'w') 
writer = csv.writer(file)
writer.writerows(csv_file)
file.close()
while i:
	
	file= open('data.csv', 'a') 
	writer = csv.writer(file)
	URL = "https://test-api.yearn.network/v1/chains/250/vaults/get"
	page = requests.get(URL)
	data=page.json()

	date = datetime.now()




	csv_data=[]
	for i in range(len(data)):

		symbol=data[i]["symbol"][2:]
		if symbol in crytos:
			lista=[]
			lista.append(symbol)
			lista.append(str(data[i]["underlyingTokenBalance"]["amountUsdc"]))
			lista.append(str(data[i]["metadata"]["apy"]["net_apy"]))
			
			lista.append(date.strftime("%d/%m/%Y, %H:%M:%S"))
			
			csv_data.append(lista)
	writer.writerows(csv_data)
	print(date)
	file.close()
	time.sleep(1200)

