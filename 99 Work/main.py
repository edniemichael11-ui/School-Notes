import csv

filepath = "student_test_scores.csv"
passed_path = "Passed.csv"
failed_path = "Failed.csv"

passed_rows = []
failed_rows = []

with open(filepath, "r", newline="") as file:
    content = csv.DictReader(file)

    for row in content:
        student = row["Student"]
        score = int(row["Test Score"])

        if score >= 70:
            passed_rows.append([student, score])
        else:
            failed_rows.append([student, score])

with open(passed_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Student", "Test Score"])
    writer.writerows(passed_rows)

with open(failed_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Student", "Test Score"])
    writer.writerows(failed_rows)S
