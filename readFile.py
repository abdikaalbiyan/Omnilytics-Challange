import csv

with open('FileChallangeA.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        
        row = row[0].replace(" ", "")

        if any(i.isdigit() for i in row):
            if "." in row:
                output = "- real numbers"
            else:
                if any(i.isalpha() for i in row):
                    output = "- alphanumeric"
                else:
                    output = "- integer"
        else:
            output = "- alphabetical strings"

        print(row, output)