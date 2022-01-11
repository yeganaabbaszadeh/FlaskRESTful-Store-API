import requests

BASE = "http://127.0.0.1:5000/"


# response = requests.post(BASE + "customer", {'name': 'Violet', 'surname': 'Evergarden', 'email': 'violet@gmail.com'})
# print(response.json())
# input()

# response = requests.post(BASE + "customer", {'name': 'Ryuzaki', 'surname': 'Lawliet', 'email': 'lawliet@gmail.com'})
# print(response.json())
# input()

# response = requests.post(BASE + "customer", {'name': 'Light', 'surname': 'Yagami', 'email': 'yagami@gmail.com'})
# print(response.json())
# input()

# # response = requests.post(BASE + "customer", {'name': 'Erika', 'surname': 'Penber', 'email': 'penber@gmail.com'})
# # print(response.json())
# # input()

# response = requests.get(BASE + "customers/1")
# print(response.json())
# input()

# response = requests.get(BASE + "customers/2")
# print(response.json())
# input()

# response = requests.delete(BASE + "customers/3")
# print(response.json())
# input()


# response = requests.post(BASE + "pc", {'cpu': 'Core i5', 'ram': '16', 'ssd': '512', 'price': 2399})
# print(response.json())
# input()

# response = requests.post(BASE + "pc", {'cpu': 'Core i7', 'ram': '8', 'ssd': '512', 'price': 2199})
# print(response.json())
# input()

# response = requests.post(BASE + "pc", {'cpu': 'Core i9', 'ram': '16', 'ssd': '512', 'price': 2899})
# print(response.json())
# input()

# # response = requests.post(BASE + "pc", {'cpu': 'Core i5', 'ram': '8', 'ssd': '512', 'price': 2199})
# # print(response.json())
# # input()

# response = requests.get(BASE + "pcs/1")
# print(response.json())
# input()

# response = requests.get(BASE + "pcs/2")
# print(response.json())
# input()

# response = requests.get(BASE + "pcs/5")
# print(response.json())
# input()

# response = requests.delete(BASE + "pcs/3")
# print(response.json())
# input()


# response = requests.post(BASE + "deal", {'customer_id': 1, 'pc_id': 1})
# print(response.json())
# input()

# response = requests.post(BASE + "deal", {'customer_id': 1, 'pc_id': 2})
# print(response.json())
# input()

# response = requests.post(BASE + "deal", {'customer_id': 2, 'pc_id': 2})
# print(response.json())
# input()

# response = requests.post(BASE + "deal", {'customer_id': 2, 'pc_id': 3})
# print(response.json())
# input()

# response = requests.post(BASE + "deal", {'customer_id': 3, 'pc_id': 3})
# print(response.json())
# input()

# response = requests.post(BASE + "deal", {'customer_id': 3, 'pc_id': 1})
# print(response.json())
# input()


response = requests.get(BASE + "/deals/showdeals/1")
print(response.json())
input()

response = requests.get(BASE + "/deals/showdeals/2")
print(response.json())
input()

# response = requests.get(BASE + "/deals/showdeals/3")
# print(response.json())
# input()

response = requests.get(BASE + "/deals/showcustomers/1")
print(response.json())
input()

response = requests.get(BASE + "/deals/showcustomers/2")
print(response.json())
input()

# response = requests.get(BASE + "/deals/showcustomers/3")
# print(response.json())
# input()