import csv

def load_csv(file_path: str):
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)  # Replace with DB insert logic


