from csv import reader, DictReader

def read_csv():
    # Context Manager
    with open(r"D:\PYTHON\Python Class\Day12 3rd Jan\covid-data.csv") as f:
        records = [ ]
        # creating object instance to reader class
        # and passing file object as a constructor argument
        # rows is iterator object
        rows = DictReader(f)
        # headers = next(rows)        # skipping the headerss
        for row in rows:
            records.append(row)
    return records
