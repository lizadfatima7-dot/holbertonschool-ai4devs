"""
Intended: Read a CSV file of student scores, compute each student's
          average, and write a new CSV with name + average columns.
Bug Type: Runtime exception + misuse of the csv library + resource leak
"""

import csv

def process_scores(input_path, output_path):
    # BUG: file opened but never closed if an exception occurs (no 'with' statement)
    infile = open(input_path, "r")
    reader = csv.reader(infile)

    results = []
    for row in reader:
        name = row[0]
        # BUG: scores are strings — summing strings concatenates them instead of adding
        scores = row[1:]                    # e.g. ['85', '90', '78']
        average = sum(scores) / len(scores) # TypeError: unsupported operand type str
        results.append([name, average])

    infile.close()

    # BUG: writer opened in "w" mode without newline="" — causes extra blank lines on Windows
    outfile = open(output_path, "w")
    writer = csv.writer(outfile)
    writer.writerow(["Name", "Average"])    # header

    # BUG: writerows expects an iterable of rows, but average is a float — will write correctly
    #      only by accident; if results is empty, no error is raised but file has only header
    for result in results:
        writer.writerow(result)

    # BUG: outfile never closed — data may not be flushed to disk
    # outfile.close() is missing


# Example usage (requires a scores.csv to exist):
# process_scores("scores.csv", "averages.csv")
process_scores("scores.csv", "averages.csv")
