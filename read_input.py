import csv

def input_to_2d_array(file_path):
    out_array = []
    with open(file_path) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            out_array.append(row)
            # print(', '.join(row))
    return out_array


def compare_dic_cat(dictionary, catlog):
    data_dict = {}

    for index in range(0, len(dictionary)):
        row = dictionary[index]
        tables = {}
        fields = set()
        if row[0] in data_dict:
            tables = data_dict[row[0]]
            if row[2] in tables:
                fields = tables[row[2]]
                fields.add(row[3])
            else:
                tables[row[2]] = set()
                fields = tables[row[2]]
                fields.add(row[3])

        else:
            data_dict[row[0]] = {}


    #print(data_dict)

    for index in range(1, len(catlog)):
        row = catlog[index]
        if row[0] in data_dict:
            tables = data_dict[row[0]]
            if row[2] in tables:
                fields = tables[row[2]]
                if not row[3] in fields:
                    print('Missing Field: ' + row[3])
            else:
                print('DB ' + row[0] + ' Missing Entity: ' + row[2])
        else:
            print('Missing DB: ' + row[0])


    # dictionary_dic={}
    # for count, q in enumerate(dictionary[1:]):
    #     key_dic = (', '.join([ q[0], q[2], q[3]]))
    #     dictionary_dic[key_dic]=q
    #     print(key_dic)
    #
    # print("----------------")
    # for count, q in enumerate(catlog[1:]):
    #     key_dic = (', '.join([, q[0], q[2], q[3]]))
    #     print(key_dic)
    return ''

print("hello")
catlog = input_to_2d_array("./catlog.csv")
dictionary = input_to_2d_array("./data_dic.csv")
dictionary2 = input_to_2d_array("./data_dic_2.csv")
compare_dic_cat(dictionary, catlog)
