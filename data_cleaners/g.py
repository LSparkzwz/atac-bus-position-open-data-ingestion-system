

with open("a.csv",'r') as f:
    with open("stop_times.csv",'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)


