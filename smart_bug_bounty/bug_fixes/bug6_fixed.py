import csv
def process_scores(input_file, output_file):
    # 'with' bloku və float çevirməsi tətbiq edildi
    with open(input_file, 'r') as f, open(output_file, 'w', newline='') as out:
        reader = csv.reader(f)
        writer = csv.writer(out)
        for row in reader:
            scores = [float(s) for s in row[1:]]
            avg = sum(scores) / len(scores)
            writer.writerow([row[0], round(avg, 2)])