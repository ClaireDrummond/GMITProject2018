import csv

with open("data/iris.csv", 'rb') as f:
    reader = csv.reader(f)
    header = next(reader)
    data_list = list(reader)
    rows = [''] + ['{:.1f}'.format(sum(float(x) for x in y) / len(data_list)) for y in zip(*data_list)[1:]]
    average_data_list = [header] + [rows]

    print (average_data_list)


    