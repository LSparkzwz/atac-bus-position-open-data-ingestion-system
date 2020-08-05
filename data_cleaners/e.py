import csv
with open("stop_times.csv","rb") as source:
    rdr= csv.reader( source )
    with open("result.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[0], r[1], r[2], r[3], r[4], r[8]) )
