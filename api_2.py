import requests
response = requests.get('https://ss.lv')
# print(response.status_code)
# print(response.text)
# print(response.json())
# print(response.headers)
# print(response.url)
# print(response.encoding)
# print(response.content)
# print(response.raw)
# print(response.raise_for_status())
# print(response.request)
# print(response.connection)
# print(response.cookies)
# print(response.elapsed)
# print(response.links)
# print(response.ok)
# print(response.reason)
# print(response.text)

query = {'q': 'BMW'}

req = requests.get('<a href="https://ss.com</a>', params=query)
req.url