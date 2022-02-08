# -------Librerias ------
import requests
from datetime import datetime
import csv
import time


# -------variables ------
crytos=["MIM", "DAI", "USDT", "USDC"]
i=True


# -------Generar CSV ------
csv_file=[["Nombre","Activos Totales","APY","Fecha"]]
file= open('data.csv', 'w') 
writer = csv.writer(file)
writer.writerows(csv_file)
file.close()


# ------- Bucle  ------
while i:
	# -------abrir CSV ------
	file= open('data.csv', 'a') 
	writer = csv.writer(file)

	# ------- pedir informacion------
	URL = "https://test-api.yearn.network/v1/chains/250/vaults/get"
	page = requests.get(URL)
	data=page.json()

	date = datetime.now()




	csv_data=[]
	# -------almacenar en variables ------
	for i in range(len(data)):

		symbol=data[i]["symbol"][2:]
		if symbol in crytos:
			lista=[]
			lista.append(symbol)
			lista.append(str(data[i]["underlyingTokenBalance"]["amountUsdc"]))
			lista.append(str(data[i]["metadata"]["apy"]["net_apy"]))
			
			lista.append(date.strftime("%d/%m/%Y, %H:%M:%S"))
			
			csv_data.append(lista)

	# -------guardar en CSV------
	writer.writerows(csv_data)
	print(date)
	file.close()
	# ------- esperar ------
	time.sleep(1200)

