import requests
import csv
import re
import os
import sys

URL = "http://localhost:3956/search"


def do_lookup(location):
    return requests.get(
        URL,
        params={
            "format": "jsonv2",
            "limit": "1",
            "q": location,
            "countrycodes": "us",
            "layer": "address",
        },
    ).json()[0]


def append_lat_lon(file_path, source, filter=""):
    good_rows = []
    bad_rows = []
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        columns = next(reader)
        for row in reader:
            row = {k: v for k, v in zip(columns, row)}
            if "complete" not in row or row["complete"] != "True":
                try:
                    print(row[source])
                    location = (
                        row[source]
                        if not filter
                        else re.findall(filter, row[source])[0]
                    )
                    location = re.sub("(SUITE|STE|APT)\s+#?\s*\w+", "", location)
                    print(location)
                    try:
                        response = do_lookup(location)
                    except:
                        response = do_lookup(','.join(location.split(',')[1:]))
                    row["complete"] = "True"
                    row["lat"] = response["lat"]
                    row["lon"] = response["lon"]
                    good_rows.append(row)
                except Exception as e:
                    print(e)
                    row["complete"] = ""
                    row["lat"] = ""
                    row["lon"] = ""
                    bad_rows.append(row)
            else:
                good_rows.append(row)
    if not "complete" in columns:
        columns.extend(["complete", "lat", "lon"])
    with open(file_path + ".tmp", "w") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        good_rows.extend(bad_rows)
        writer.writerows([[r[k] for k in columns] for r in good_rows])
    os.rename(file_path + ".tmp", file_path)


if __name__ == "__main__":
    append_lat_lon(sys.argv[1], sys.argv[2], sys.argv[3])
