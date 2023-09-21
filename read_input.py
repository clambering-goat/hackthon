import csv
import matplotlib.pyplot as plt
import numpy as np
from gen_png_chart import *
output = {}


def input_to_2d_array(file_path):
    out_array = []
    with open(file_path) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            out_array.append(row)
    return out_array


def create_dic_for_input(data):
    data_dict = {}

    for index in range(1, len(data)):
        row = data[index]
        tables = {}
        fields = set()

        db_name = row[0]
        table_name = row[2]
        field_name = row[3]

        if not db_name in data_dict:
            data_dict[db_name] = {}

        tables = data_dict[db_name]
        if not table_name in tables:
            tables[table_name] = set()

        fields = tables[table_name]
        fields.add(field_name)

    return data_dict


def calculate_field_level(dict, cat, name):
    print(name)
    total = 0
    found = 0
    for field in cat:
        total = total + 1
        if field in dict:
            found = found + 1
    rs = found*100/total
    print("Completeness of the table: " + str(rs) + " %\n")
    output[name] = rs

def calculate_completeness(dictionary, catalog):
    # Get db name
    my_db_name = list(dictionary.keys())[0]
    # Get catalog for dict
    my_cat = catalog[my_db_name]
    total = 0
    found = 0
    for table in my_cat:
        total = total + 1
        if table in dictionary[my_db_name]:
            print("Found " + table)
            calculate_field_level(
                dictionary[my_db_name][table], my_cat[table], table)
            found = found + 1
        else:
            print("Not found " + table)
    rs = found * 100 / total
    print("\nCompleteness of the db: " + str(rs) + " %")
    output[my_db_name] = rs
    print(output)
    gen_chart(["Done", "Not done"], [rs, 100-rs], "database.png")


catalog_arr = input_to_2d_array("./catlog.csv")
catalog_dict = create_dic_for_input(catalog_arr)

dict_files = ["./data_dic.csv"]
# dict_files = ["./data_dic.csv", "./data_dic_2.csv"]

for file in dict_files:
    dictionary_arr = input_to_2d_array(file)
    dictionary_dict = create_dic_for_input(dictionary_arr)
    calculate_completeness(dictionary_dict, catalog_dict)
