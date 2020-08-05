import csv
import json
from ast import literal_eval

with open("bus_feed.csv","rb") as source:
    rdr= csv.reader( source )
    with open("bus_feed.json","wb") as result:
        wtr= csv.writer( result )
        map = {}
        skip = True
        for r in rdr:
            value = []
            if skip:
                skip = False
            elif r[0] != "":    
                if r[0] in map:
                    arr = literal_eval(r[3])
                    value.append(r[2])
                    value.append(arr)
                    map[r[0]][r[1]] = value
                else:
                    map[r[0]] = {}    
                    arr = literal_eval(r[3])
                    value.append(r[2])
                    value.append(arr)
                    map[r[0]][r[1]] = value
            

        json.dump(map, result)
