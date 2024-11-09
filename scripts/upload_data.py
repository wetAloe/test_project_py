import requests
import csv


with open("data/images.csv", "r") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i == 0:
            continue

        if row[0] == "":
            continue

        data = list(map(int, row[1:]))
        requests.post("http://localhost:8000/upload_image", json={"data": data})
