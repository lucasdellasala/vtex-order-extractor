import json
import requests
import csv

print("Enter your cookies: \n")
cookies_input = input()

lines = csv.reader(open('paso2.csv', 'r'), lineterminator='\n')

url_transactions = 'https://mcdar.myvtex.com/api/payments/pvt/admin/transactions/'
url_end = '/payments'
cookies = dict(VtexIdclientAutCookie=cookies_input)

c= csv.writer(open("final.csv", "w"), lineterminator='\n')

i=1

for line in lines:
    orderId = line[0]
    sequence = line[1]
    sellerOrderId = line[2]
    hostname = line[3]
    sellersId = line[4]
    status = line[5]
    creationDate_date = line[6]
    creationDate_time = line[7]
    email = line[8]
    firstName = line[9]
    lastName = line[10]
    document = line[11]
    transactionId = line[12]
    payments_Id = line[13]
    payments_paymentSystemName = line[14]
    payments_group = line[15]
    payments_value = line[16]
    payments_installments = line[17]
    payments_referenceValue = line[18]
    payments_connectorResponses_Tid = line[19]
    payments_connectorResponses_ReturnCode = line[20]
    payments_connectorResponses_acquirer = line[21]
    payments_connectorResponses_message = line[22]

    if line[22]=="null":
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
		payments_connectorResponses_Tid,
		payments_connectorResponses_ReturnCode,
		payments_connectorResponses_acquirer,
		payments_connectorResponses_message
    ])

    print(str(i)+"/1745")
    print("\n")
    i+=1