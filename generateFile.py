import os
import csv
import random
from generateRandom import GenerateRandom

generate = GenerateRandom()

limit = 10485760 #10MB

with open('FileChallangeA.csv', 'w') as csv_file:
    csv_writer      = csv.writer(csv_file)

    currentSize     = 0
    while currentSize < limit:
        alphaString = generate.randomAlphaString(0,25)
        realNum     = generate.randomRealNumber(0.1, 20.9)
        integers    = generate.randomIntegers(0, 100000)
        alphaNum    = generate.randomAlphaNum(0,25)

        randomVar   = random.choice([alphaString, realNum, integers, alphaNum])

        if randomVar== alphaNum:
            data    = alphaNum
            space   = random.randint(0, 9)
            data    = ' ' * space + data + ' ' * space
        else:
            data    = randomVar

        csv_writer.writerow([data])

        currentSize = os.stat('FileChallangeA.csv').st_size

print("File Created")