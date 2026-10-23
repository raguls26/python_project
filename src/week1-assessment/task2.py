
from pathlib import Path
import csv
import json

# Find employees.csv in the same folder as task2.py
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "employees.csv"

employees = []

with csv_path.open("r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    print("CSV columns:", reader.fieldnames)

    for row in reader:
        row["id"] = int(row["id"])
        row["salary"] = float(row["salary"])
        employees.append(row)

print("Rows read:", len(employees))

with open(BASE_DIR / "employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

print("employees.json created successfully")

high_earners = [emp for emp in employees if emp["salary"] > 50000]

with open(BASE_DIR / "high_earners.csv", "w", newline="", encoding="utf-8") as file:
    fields = ["id", "name", "department", "salary", "city"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(high_earners)

print("High earners:", len(high_earners))
print("high_earners.csv created successfully")
