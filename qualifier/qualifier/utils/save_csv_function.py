import csv


def save_csv(csvpath, data):
    with open(csvpath, 'w') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter=",")
        for datum in data:
            csvwriter.writerow(datum)