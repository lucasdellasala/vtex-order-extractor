import csv
import requests
import json

print("Enter your cookies: \n")
cookies_input = input()
print("Enter the account name:\n")
account= input()
print("Do you want incomplete orders?\n write 'true' if you want, and 'false' if not.\n")
incompleteOrders= input()
url_list = 'https://'+account+'.vtexcommercestable.com.br/api/oms/pvt/orders?per_page=100&f_creationDate=creationDate:[2021-03-01T03:00:00.000Z TO 2021-03-11T02:59:59.000Z]&incompleteOrders='+incompleteOrders+'&per_page=100'
cookies = dict(VtexIdclientAutCookie=cookies_input)
pages = 0

def obtener_lista():
        #Traer página
        r = requests.get(url_list, cookies=cookies).json() 
        pages = int(r['paging']['pages'])
        
        c= csv.writer(open("paso1.csv", "w"), lineterminator='\n')

        for response in range(1, pages+1):

                new_url = url_list + '&page=' + str(response) 

                new_r = requests.get(new_url, cookies=cookies).json()
                print(str(response)+"/"+str(pages))

                for item in new_r['list']:

                        content = json.dumps(item)
   
                        c.writerow([
                        item['orderId'],
                        content
                        ])


obtener_lista()
#number_pages = 117