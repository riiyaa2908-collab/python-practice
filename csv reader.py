import csv
header = ["Name", "Marks", "City"]
rows= [ ["Amit","85","Delhi"], ["Priya","92","Mumbai"], ["Rahul","78","Pune"], ["Sara","88","Jaipur"] ]
with open('data.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)
    csv_writer.writerows(rows)
    print("CSV file created successfully.")

with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    total= 0
    count= 0
    
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        marks = int(row[1])
        total += marks
        count +=1
        print(f"{row[0]} Scored {row[1]} and lives in {row[2]}")
    Toppers = list(filter(lambda row: int(row[1]) > 80, rows))
    for row in Toppers:
        print(f"{row[0]} Scored above 80")
print(f"Total marks: {total}")
print(f"Average marks: {total/count}")