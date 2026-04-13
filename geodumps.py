import sqlite3
import json

count = 0

with sqlite3.connect('opengeo.sqlite') as conn:
    cur = conn.cursor()

    rows = cur.execute('SELECT * FROM Locations')
    # print(row)

    with open('where.js', 'w', encoding='UTF-8') as f:
        f.write('Data = [\n')

        for row in rows:
            if count >= 1:
                break
            geodata = row[1].decode()
            try:
                dict_data = json.loads(geodata)
            except Exception:
                continue
            
            # print(dict_data)
            
            if not dict_data or 'features' not in dict_data:
                print('error in downloading')
                break

            if len(dict_data['features']) == 0:
                print('invalid data')
                continue

            try:
                lon = dict_data['features'][0]['properties']['lon']
                lat = dict_data['features'][0]['properties']['lat']
                where = dict_data['features'][0]['properties']['display_name'].replace("'","")
                
            except Exception:
                continue

            
            print(f'longitude: {lon}')
            print(f'latitude: {lat}')
            print(f'place: {where}')

            line = f"[{str(lon)}, {str(lat)}, '{str(where)}'],\n"
            f.write(line)
            
            # count += 1
        f.write(']')