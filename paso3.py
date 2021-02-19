import json
import requests
import csv

print("Enter your cookies: \n")
cookies_input = input()

lines = csv.reader(open('paso2.csv', 'r'), lineterminator='\n')

url_transactions = 'https://mcdecflexuat.myvtex.com/api/payments/pvt/admin/transactions/'
url_end = '/payments'
cookies = dict(VtexIdclientAutCookie=cookies_input)

c= csv.writer(open("final.csv", "w"), lineterminator='\n')

i=1

for line in lines:
    orderId = line[0]
    url = line[1]
    sequence = line[2]
    sellerOrderId = line[3]
    hostname = line[4]
    sellersId = line[5]
    status = line[6]
    creationDate_date = line[7]
    creationDate_time = line[8]
    email = line[9]
    firstName = line[10]
    lastName = line[11]
    document = line[12]
    transactionId = line[13]
    payments_Id = line[14]
    payments_paymentSystemName = line[15]
    payments_group = line[16]
    payments_value = line[17]
    payments_installments = line[18]
    payments_referenceValue = line[19]
    payments_lastDigits = line[20]
    payments_connectorResponses_Tid = line[21]
    payments_connectorResponses_ReturnCode = line[22]
    payments_connectorResponses_acquirer = line[23]
    payments_connectorResponses_message = line[24]

    if line[24]=="null":
        new_url = url_transactions + transactionId + url_end
        r = requests.get(new_url, cookies=cookies).json()
        try:            
            length = int(len(r[0]['fields']))
            position = length - 1
            value = r[0]['fields'][position]['value']
            value_json = json.loads(value)
            payments_connectorResponses_message = value_json['message']
        except:
            payments_connectorResponses_message = "API ERROR: "+ str(r)
        
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

    print(str(i)+"/1380")
    print("\n")
    i+=1