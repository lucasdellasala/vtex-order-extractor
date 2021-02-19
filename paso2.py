import requests
import csv
import json
import dateutil.parser
import datetime

print("Enter your cookies: \n")
cookies_input = input()

lines = csv.reader(open('paso1.csv', 'r'), lineterminator='\n')

url_order = 'https://mcdecflexuat.vtexcommercestable.com.br/api/oms/pvt/orders/'
cookies = dict(VtexIdclientAutCookie=cookies_input)

c= csv.writer(open("paso2.csv", "w"), lineterminator='\n')

c.writerow([
		'orderId',
		'url',
		'sequence',
		'sellerOrderId',
		'hostname',
		'sellers_id',
		'status',
		'creationDate(date)',
		'creationDate(time)',
		'email',
		'firstName',
		'lastName',
		'document',
		'transactionId',
		'payments_id',
		'payments_paymentSystemName',
		'payments_group',
		'payments_value',
		'payments_installments',
		'payments_referenceValue',
		'payments_lastDigits',
		'payments_connectorResponses_Tid',
		'payments_connectorResponses_ReturnCode',
		'payments_connectorResponses_acquirer',
		'payments_connectorResponses_message'
])

i=1

for line in lines:
	#if i<341:
	#	i+=1
	#	continue
		
	print(str(i)+"/1381")
	print("Id: "+ line[0])
	print('\n')

	content = line[1]
	new_url = url_order+line[0]
	content = json.loads(content)

	r = requests.get(new_url, cookies=cookies).json()
	
	# Comienzo a crear los valores de las columnas
	orderId = line[0]
	sequence = content['sequence']
	sellerOrderId = r['sellerOrderId']
	hostname = content['hostname']
	sellersId = r['sellers'][0]['id']
	status = r['status']

	# Dia y hora
	creationDate = content['creationDate']
	creationDate = dateutil.parser.parse(creationDate)
	
	# Convierto a UTC_3
	timedeltaARG = datetime.timedelta(hours = 3)
	creationDateARG = creationDate - timedeltaARG
	
	creationDate_date = creationDateARG.date()
	creationDate_time = creationDateARG.time()

	# Continuo con el resto de las columnas
	email = r['clientProfileData']['email']
	firstName = r['clientProfileData']['firstName']
	lastName = r['clientProfileData']['lastName']
	document = r['clientProfileData']['document']
	transactionId = r['paymentData']['transactions'][0]['transactionId']
		
	url_seller_used = False

	try:
		print('NewUrl')
		print(new_url)
		payments_Id = r['paymentData']['transactions'][0]['payments'][0]['id']
		payments_paymentSystemName = r['paymentData']['transactions'][0]['payments'][0]['paymentSystemName']
		payments_group = r['paymentData']['transactions'][0]['payments'][0]['group']
		payments_value = r['paymentData']['transactions'][0]['payments'][0]['value']
		payments_installments = r['paymentData']['transactions'][0]['payments'][0]['installments']
		payments_referenceValue = r['paymentData']['transactions'][0]['payments'][0]['referenceValue']
		payments_lastDigits = r['paymentData']['transactions'][0]['payments'][0]['lastDigits']
		payments_connectorResponses_Tid = r['paymentData']['transactions'][0]['payments'][0]['connectorResponses']['Tid']
		payments_connectorResponses_ReturnCode = r['paymentData']['transactions'][0]['payments'][0]['connectorResponses']['ReturnCode']
		payments_connectorResponses_acquirer = r['paymentData']['transactions'][0]['payments'][0]['connectorResponses']['acquirer']
		payments_connectorResponses_message = r['paymentData']['transactions'][0]['payments'][0]['connectorResponses']['message']
	except:
		try:
			url_seller = 'https://'+sellersId+'.vtexcommercestable.com.br/api/oms/pvt/orders/'+sellerOrderId
			url_seller_used = True
			print('UrlSeller')
			print(url_seller)
			r_seller = requests.get(url_seller, cookies=cookies).json()
			status = r_seller['status']
			payments_Id = r_seller['paymentData']['transactions'][0]['payments'][0]['id']
			payments_paymentSystemName = r_seller['paymentData']['transactions'][0]['payments'][0]['paymentSystemName']
			payments_group = r_seller['paymentData']['transactions'][0]['payments'][0]['group']
			payments_value = r_seller['paymentData']['transactions'][0]['payments'][0]['value']
			payments_installments = r_seller['paymentData']['transactions'][0]['payments'][0]['installments']
			payments_referenceValue = r_seller['paymentData']['transactions'][0]['payments'][0]['referenceValue']
			payments_lastDigits = r_seller['paymentData']['transactions'][0]['payments'][0]['lastDigits']
			payments_connectorResponses_Tid = r_seller['paymentData']['transactions'][0]['payments'][0]['connectorResponses']['Tid']
			payments_connectorResponses_ReturnCode = r_seller['paymentData']['transactions'][0]['payments'][0]['connectorResponses']['ReturnCode']
			payments_connectorResponses_acquirer = r_seller['paymentData']['transactions'][0]['payments'][0]['connectorResponses']['acquirer']
			payments_connectorResponses_message = r_seller['paymentData']['transactions'][0]['payments'][0]['connectorResponses']['message']

		except:
			payments_connectorResponses_Tid = "No payment data"
			payments_connectorResponses_ReturnCode = "No payment data"
			payments_connectorResponses_message = "No payment data"
			payments_connectorResponses_acquirer = "No payment data"

	if payments_connectorResponses_message is None:
		payments_connectorResponses_message = "null"

	#Si algún valor es null le asigno el string "null" si no queda vacío el campo en la fila
	sequence = "null" if sequence is None else sequence
	sellerOrderId = "null" if sellerOrderId is None else sellerOrderId
	hostname = "null" if hostname is None else hostname
	sellersId = "null" if sellersId is None else sellersId
	status = "null" if status=="" else status
	creationDate_date = "null" if creationDate_date is None else creationDate_date
	creationDate_time = "null" if creationDate_time is None else creationDate_time
	email = "null" if email is None else email
	firstName = "null" if firstName is None else firstName
	lastName = "null" if lastName is None else lastName
	document = "null" if document is None else document
	transactionId = "null" if transactionId is None else transactionId
	payments_Id = "null" if payments_Id is None else payments_Id
	payments_paymentSystemName = "null" if payments_paymentSystemName is None else payments_paymentSystemName
	payments_group = "null" if payments_group is None else payments_group
	payments_value = "null" if payments_value is None else payments_value
	payments_installments = "null" if payments_installments is None else payments_installments
	payments_referenceValue = "null" if payments_referenceValue is None else payments_referenceValue
	payments_lastDigits = "null" if payments_lastDigits is None else payments_lastDigits
	payments_connectorResponses_Tid = "null" if payments_connectorResponses_Tid is None else payments_connectorResponses_Tid
	payments_connectorResponses_ReturnCode = "null" if payments_connectorResponses_ReturnCode is None else payments_connectorResponses_ReturnCode
	payments_connectorResponses_acquirer = "null" if payments_connectorResponses_acquirer is None else payments_connectorResponses_acquirer 
	payments_connectorResponses_message = "null" if payments_connectorResponses_message is None else payments_connectorResponses_message 
	
	#Creo la url (nueva columna) para poder consultarla individualmente con postman
	print(url_seller_used)
	print('\n')
	if url_seller_used is False:
		url = new_url
	else:
		url = url_seller
	
	#Escribo cada columna para una fila
	c.writerow([
		orderId,
		url,
		sequence,
		sellerOrderId,
		hostname,
		sellersId,
		status,
		creationDate_date,
		creationDate_time,
		email,
		firstName,
		lastName,
		document,
		transactionId,
		payments_Id,
		payments_paymentSystemName,
		payments_group,
		payments_value,
		payments_installments,
		payments_referenceValue,
		payments_lastDigits,
		payments_connectorResponses_Tid,
		payments_connectorResponses_ReturnCode,
		payments_connectorResponses_acquirer,
		payments_connectorResponses_message
	])

	i+=1