import csv


def parse(file_path):
    csv_data = []
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # csv_reader = list(csv.reader(csv_file))
        for row in csv_reader:
            # print(row)
            csv_data.append(dict(row))
    return csv_data
