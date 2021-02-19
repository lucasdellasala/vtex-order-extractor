import csv
import requests
import json

print("Enter your cookies: \n")
cookies_input = input()

url_list = 'https://mcdecflexuat.vtexcommercestable.com.br/api/oms/pvt/orders?per_page=100&f_creationDate=creationDate:[2021-01-24T03:00:00.000Z TO 2021-02-01T02:59:59.000Z]&incompleteOrders=false&per_page=100'
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