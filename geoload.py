import json
import sqlite3
import ssl
import urllib.request, urllib.error, urllib.parse
import time

main_url = 'https://py4e-data.dr-chuck.net/opengeo?'
parmater = {}
count = 0
notfound = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with sqlite3.connect('opengeo.sqlite') as conn:
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)')

    with open('where.data', 'r', encoding='UTF-8') as f:
        content = f.read().strip()
        # print(content)
        if content == None:
            print('file is empty')
            quit()
        f.seek(0)

        for address in f:
            if count > 100:
                break
            if len(address) <= 1:
             continue
            address = address.strip()

            try:
                geodata = cur.execute('SELECT geodata FROM Locations WHERE address = ?', (address, )).fetchone()[0]
                print('Data existed in the database')
                continue
            except:
                pass

            parmater['q'] = address
            url = main_url + urllib.parse.urlencode(parmater)

            response = urllib.request.urlopen(url, context=ctx)
            data = response.read().decode()
            print(f'retrieving {url}')
            count += 1

            try:
                dict_data = json.loads(data)
            except:
                continue

            if not dict_data or 'features' not in dict_data:
                print('Download Error')
                print(data)
                break

            if len(dict_data['features']) == 0 :
                print('object not found')
                notfound += 1

            cur.execute('INSERT INTO Locations (address, geodata) VALUES (?, ?)', (memoryview(address.encode()), memoryview(data.encode())))
            

            if count % 10 == 0:
                print('==pause==')
                time.sleep(5)

if notfound > 1:
    print(f'the number of locations we have not retrieved: {notfound}')


