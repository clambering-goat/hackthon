import csv
from gen_png_chart import generate_pie_chart

# Column orders to extract info
DB_INDEX = 0
ENTITY_INDEX = 2
ATTRIBUTE_INDEX = 3

stats = []
missing = []


def read_csv_to_array(file_path):
    out_array = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            out_array.append(row)
    return out_array


def build_dictionary_from_array(array, db_index, entity_index, attribute_index):
    data_dict = {}
    for index in range(1, len(array)):
        row = array[index]
        db_name = row[db_index]
        entity_name = row[entity_index]
        attribute_name = row[attribute_index]

        if not db_name in data_dict:
            data_dict[db_name] = {}

        entities = data_dict[db_name]
        if not entity_name in entities:
            entities[entity_name] = set()

        attributes = entities[entity_name]
        attributes.add(attribute_name)

    return data_dict


def calculate_completeness_at_attribute_level(dictionary, catalog, entity_name, db_name):
    total = 0
    found = 0
    for attribute in catalog:
        total = total + 1
        if attribute in dictionary:
            found = found + 1
        else:
            missing.append("Database " + db_name + ", entity " +
                           entity_name + " missing attribute " + attribute)
    completeness = round(found * 100 / total, 2)
    print(f"Completeness of the entity {entity_name}: {str(completeness)}.")
    stats.append({'label': entity_name, 'value': completeness})


def calculate_completeness(dictionary, catalog, save_chart):
    stats.clear()
    missing.clear()
    db_name = list(dictionary.keys())[0]
    total = 0
    found = 0
    for entity in catalog:
        total = total + 1
        if entity in dictionary[db_name]:
            calculate_completeness_at_attribute_level(
                dictionary[db_name][entity], catalog[entity], entity, db_name)
            found = found + 1
        else:
            stats.append({'label': entity, 'value': 0})
            missing.append("Database " + db_name +
                           " missing entity " + entity)
    completeness = round(found * 100 / total, 2)
    print(f"Completeness of the database {db_name}: {str(completeness)}%")
    stats.append({'label': db_name, 'value': completeness})
    if save_chart:
        generate_pie_chart(["Done", "Not done"], [completeness, 100-completeness], db_name + ".png")
    return {"stats": stats, "missing": missing}


def compare(db_index, entity_index, attribute_index):
    full_catalog_arr = read_csv_to_array("./uploads/csv/catalog.csv")
    full_catalog_dict = build_dictionary_from_array(full_catalog_arr, db_index, entity_index, attribute_index)

    db_dictionary_arr = read_csv_to_array("./uploads/csv/dictionary.csv")
    db_dictionary_dict = build_dictionary_from_array(db_dictionary_arr, db_index, entity_index, attribute_index)

    db_name = list(db_dictionary_dict.keys())[0]
    db_catalogue_dict = full_catalog_dict[db_name]
    rs = calculate_completeness(db_dictionary_dict, db_catalogue_dict, False)
    print(rs)
    return rs


def main(db_index, entity_index, attribute_index):
    full_catalog_arr = read_csv_to_array("./catlog.csv")
    full_catalog_dict = build_dictionary_from_array(full_catalog_arr, db_index, entity_index, attribute_index)

    # dict_files = ["./data_dic.csv"]
    dict_files = ["./data_dic.csv", "./data_dic_2.csv"]

    for file in dict_files:
        db_dictionary_arr = read_csv_to_array(file)
        db_dictionary_dict = build_dictionary_from_array(db_dictionary_arr, db_index, entity_index, attribute_index)

        db_name = list(db_dictionary_dict.keys())[0]
        db_catalogue_dict = full_catalog_dict[db_name]

        rs = calculate_completeness(db_dictionary_dict, db_catalogue_dict, True)
        print(rs)


print(main(DB_INDEX, ENTITY_INDEX, ATTRIBUTE_INDEX))  # Just for testing without starting the microservice
