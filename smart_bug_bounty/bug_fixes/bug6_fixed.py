import csv

def process_scores(input_file, output_file):
    # 'with' bloku istifadə edilərək fayl sızması düzəldildi
    with open(input_file, 'r') as f, open(output_file, 'w', newline='') as out:
        reader = csv.reader(f)
        writer = csv.writer(out)
        for row in reader:
            name = row[0]
            # String dəyərlər float-a çevrildi
            scores = [float(s) for s in row[1:]]
            avg = sum(scores) / len(scores)
            writer.writerow([name, round(avg, 2)])