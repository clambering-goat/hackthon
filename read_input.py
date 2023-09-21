import csv
print('hello')
file_path = "../catlog.csv"
out_array = []
with open(file_path, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        out_array.append(out_array)
        # print(', '.join(row))

print(out_array)

for count_1, q in enumerate(out_array):
    for count_2, w in enumerate(q):
        if w is None:
            print("hi")

print("done")
