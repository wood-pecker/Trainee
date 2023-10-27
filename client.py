import requests

login = input('Login: ')
password = input('Password: ')

data = {'login': login, 'password': password}
requests.post('http://127.0.0.1:5000/login', json=data)
