#---AlluKoodaa---#

from urllib.request import urlopen
import json
from datetime import datetime


def get_intel():
    url = "192.168.1.94/api/v1/stats"

    with urlopen(url) as response:
        body = response.read()

###    with open("test_filee.json") as file:
###        body = file.read()
        
    return json.loads(body)

def read_file(file):
    data = {}
    try:
        with open(file) as file:
            for row in file:
                parts = row.strip().split(";")
                if parts[0] == "Date":
                    dates = parts[1:]
                    continue
                data[parts[0]] = parts[1:]
    except FileNotFoundError:
        return None, None

    return data, dates

def write_file(file, dates, data: dict):
    header = ""
    for date in dates:
        header += ";" + date
    with open(file, "w") as csv:
        csv.write(f"Date{header}\n")
        for key, value in data.items():
            row_string = ""
            for x in value:
                row_string += ";" + str(x)
            csv.write(f"{key}{row_string}\n")

    return None

def write_new_file(file, date, data: dict):
    with open(file, "w") as tdst:
        tdst.write(f"Date;{date}\n")
        for key, value in data.items():
            tdst.write(f"{key};{value}\n")
    
def main():
    timestamp = datetime.now().strftime("%d/%m/%Y")
###    timestamp = "20/07/2022"
    file = "tiedot.csv"
    new_data = get_intel()
    data, dates = read_file(file)
    if data:
        for key, value in new_data.items():
            if key != "Date":
                data[key] += [value]
        dates.append(timestamp)
        write_file(file, dates, data)
    else:
        write_new_file(file, timestamp, new_data)

    return None

main()

#---eof---#
