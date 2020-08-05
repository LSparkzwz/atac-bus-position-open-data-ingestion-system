import csv
import json
from ast import literal_eval

with open("shapes.csv","rb") as source:
    rdr= csv.reader( source )
    with open("shapes.json","wb") as result:
        wtr= csv.writer( result )
        map = {}
        skip = True
        for r in rdr:
            value = []
            if skip:
                skip = False
            else:    
                arr = literal_eval(r[1])
                for v in arr:
                    value.append([v[0],v[1],v[2],v[3]])
            map[r[0]] = value
            

        json.dump(map, result)
