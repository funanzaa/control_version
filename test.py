from urllib.request import Request, urlopen
import requests

# __domain__ = 'http://61.19.253.23'
__domain__ = 'http://localhost:8000'

serverVersionAutoUpdate = __domain__ + '/media/file/version_AppAutoUpdate.txt'

r = requests.get(serverVersionAutoUpdate)
print(r.text)
