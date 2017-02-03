import csv
from collections import defaultdict


# Column indexes on CSV file.
TOTAL = 1
ADVERTISER = 2
CAMPAIGN = 3
MEDIUM = 4


def compute_from(file):
    advertisers = defaultdict(int)
    campaigns = defaultdict(int)
    media = defaultdict(int)
    total = 0

    with open(file, newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader) # Skips headers row.
        for row in reader:
            amount = float(row[TOTAL])
            advertisers[row[ADVERTISER]] += amount
            campaigns[row[CAMPAIGN]] += amount
            media[row[MEDIUM]] += amount
            total += amount
    
    return advertisers, campaigns, media, total
