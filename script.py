import hashlib
import requests

for i in range(0,100):
    linkid = hashlib.md5()
    linkid.update(bytes(str(i), 'utf-8'))
    rid = linkid.hexdigest()
    url = f'http://10.10.115.94/{rid}'

    response = requests.get(url)
    if response.status_code != 200:
        pass
    else:
        print(f"HASH IS:{rid}\nID is: {i}")


