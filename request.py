import requests

BASE = "http://127.0.0.1:5000/"

'''
response = requests.post(BASE + "customer", {'name': 'Yegana', 'surname': 'Abbaszadeh', 'email': 'yegana@gmail.com'})
print(response.json())
input()

response = requests.post(BASE + "customer", {'name': 'Sevar', 'surname': 'Jafarli', 'email': 'sevar@gmail.com'})
print(response.json())
input()

response = requests.post(BASE + "customer", {'name': 'Asmar', 'surname': 'Hajizadeh', 'email': 'asmar@gmail.com'})
print(response.json())
input()


response = requests.get(BASE + "customers/1")
print(response.json())
input()

response = requests.get(BASE + "customers/2")
print(response.json())
input()

response = requests.get(BASE + "customers/3")
print(response.json())
input()

# response = requests.delete(BASE + "customers/3")
# print(response.json())
# input()

response = requests.post(BASE + "pc", {'cpu': 'Core i5', 'ram': '8', 'ssd': '256', 'price': 1500})
print(response.json())
input()

response = requests.post(BASE + "pc", {'cpu': 'Core i7', 'ram': '8', 'ssd': '512', 'price': 2500})
print(response.json())
input()

response = requests.post(BASE + "pc", {'cpu': 'Core i9', 'ram': '16', 'ssd': '512', 'price': 3500})
print(response.json())
input()


response = requests.get(BASE + "pcs/1")
print(response.json())
input()

response = requests.get(BASE + "pcs/2")
print(response.json())
input()

response = requests.get(BASE + "pcs/3")
print(response.json())
input()

# response = requests.delete(BASE + "pcs/3")
# print(response.json())
# input()


response = requests.post(BASE + "deal", {'customer_id': 1, 'pc_id': 1})
print(response.json())
input()

response = requests.post(BASE + "deal", {'customer_id': 1, 'pc_id': 2})
print(response.json())
input()

response = requests.post(BASE + "deal", {'customer_id': 1, 'pc_id': 3})
print(response.json())
input()

response = requests.post(BASE + "deal", {'customer_id': 2, 'pc_id': 2})
print(response.json())
input()

response = requests.post(BASE + "deal", {'customer_id': 2, 'pc_id': 3})
print(response.json())
input()

response = requests.post(BASE + "deal", {'customer_id': 3, 'pc_id': 3})
print(response.json())
input()


response = requests.get(BASE + "deals/showdeals/1")
print(response.json())
input()

response = requests.get(BASE + "deals/showdeals/2")
print(response.json())
input()

response = requests.get(BASE + "deals/showdeals/3")
print(response.json())
input()

response = requests.get(BASE + "deals/showcustomers/1")
print(response.json())
input()

response = requests.get(BASE + "deals/showcustomers/2")
print(response.json())
input()

response = requests.get(BASE + "deals/showcustomers/3")
print(response.json())
input()
'''

response = requests.get(BASE + "bestbuyer")
print(response.json())
input()
