import csv
import json
from ast import literal_eval

with open("stop_data.csv","rb") as source:
    rdr= csv.reader( source )
    with open("stop_data.json","wb") as result:
        wtr= csv.writer( result )
        map = {}
        aliases = {}
        skip = True
        key = 0
        for r in rdr:
            if skip:
                skip = False
            elif r[0] != "":    
                 value = []
                 trip_ids = literal_eval(r[0])
                 for t in trip_ids:
                      aliases[t] = key
                 value.append(literal_eval(r[1]))
                 value.append(r[2])
                 value.append(r[3])
                 value.append(r[4])
                 value.append(r[5])
                 map[key] = value
                 key = key + 1
            

        json.dump(map, result)
    with open("aliases.json","wb") as o:
        json.dump(aliases, o)
