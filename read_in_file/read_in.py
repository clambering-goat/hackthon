import csv
import re
import os


def find_file():
    path_to_look_at = input("what is the dir location of the files")
    # path_to_look_at="C:/Users/camer/PycharmProjects/hackthon"
    path_to_look_at = "/Users/trien/Repos/hackthon"
    dir = os.scandir(path_to_look_at)
    print("file found")
    for count, q in enumerate(dir):
        print(count, q.name)



def print_out_put_data(data):
    print("--------------------")
    for q in data:
        print(q)





def print_out_put_data_2(data):
    print("--------------------")
    for q in data:
        print(q, data[q])


def fullneses(data):

    data_fullness={}
    dictionary_dic = {}
    for count, q in enumerate(data):
        key_dic = ('###'.join([data[q][0], data[q][2]]))
        if not key_dic in dictionary_dic:
            dictionary_dic[key_dic] = []
        dictionary_dic[key_dic].append(data[q])
    tale_look = {}
    for q in dictionary_dic:
        full_size = len(dictionary_dic[q])
        less = 0
        for w in dictionary_dic[q]:
            if len(w) > 6:
                less = less + 1

        print(q, (less / full_size) * 100)
        tale_look[q] = (less / full_size) * 100
    db_summary = {}
    count = {}
    for q in tale_look:
        keys = q.split("###")[0]
        if not keys in db_summary:
            db_summary[keys]=0
            count[keys]=0
        db_summary[keys]= db_summary[keys]+ tale_look[q]
        count[keys]=count[keys]+1

    for q in db_summary:
        print(q, (db_summary[q]/count[keys]))
        data_fullness[q]=((db_summary[q]/count[keys]))

    return(data_fullness)
    print("done")



def Filter(string):
    out_array = []
    for q in string:
        hold = re.findall(r"[A-z1-9]+", q)
        out_array.append((''.join(hold)))
    out_array = list(filter(lambda a: a != "", out_array))

    return out_array


def input_to_2d_array(file_path):
    # file_path = "catlog.csv"
    out_array = []
    with open(file_path) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            row = Filter(row)
            out_array.append(row)
            # print(', '.join(row))
    return out_array






def compare_dic_cat(dictionary, catlog):
    dictionary_dic = {}
    for count, q in enumerate(dictionary[1:]):
        key_dic = ('###'.join([q[0], q[2], q[3]]))
        dictionary_dic[key_dic] = q

    catlog_dic = {}
    for count, q in enumerate(catlog[1:]):
        key_dic = ('###'.join([q[0], q[2], q[3]]))

        catlog_dic[key_dic] = q

    out_put_data = {}
    joined_data_array = []
    for q in catlog_dic:
        if q in dictionary_dic:
            joined_data_array = catlog_dic[q]
            joined_data_array.append(dictionary_dic[q][-1])
        else:
            joined_data_array = catlog_dic[q]

        # joined_data_array.append(q)
        out_put_data[q] = (joined_data_array)
    print_out_put_data(out_put_data)
    return out_put_data


# got


def update_out_put(update_out_put, dictionary):
    dictionary_dic = {}
    for count, q in enumerate(dictionary[1:]):
        key_dic = ('###'.join([q[0], q[2], q[3]]))
        dictionary_dic[key_dic] = q
        print(key_dic)

    for q in update_out_put:
        if q in dictionary_dic:
            update_out_put[q].append(dictionary_dic[q][-1])
    print_out_put_data_2(update_out_put)
    return (update_out_put)




if __name__ == "__main__":
    catlog = input_to_2d_array("../put_catlog_here/catlog.csv")
    dictionary = input_to_2d_array("../put_dic_here/data_dic.csv")

    joined_data_array = compare_dic_cat(dictionary, catlog)
    dictionary2 = input_to_2d_array("../put_dic_here/data_dic_2.csv")

    joined_data_array = update_out_put(joined_data_array, dictionary2)

    fullneses(joined_data_array)


def run_get_array_data():
    catlog = input_to_2d_array("../put_catlog_here/catlog.csv")
    dictionary = input_to_2d_array("../put_dic_here/data_dic.csv")

    joined_data_array = compare_dic_cat(dictionary, catlog)
    dictionary2 = input_to_2d_array("../put_dic_here/data_dic_2.csv")

    joined_data_array = update_out_put(joined_data_array, dictionary2)

    db_data=fullneses(joined_data_array)
    has_data=[]
    missing_data=[]
    for q in joined_data_array:
        if len(joined_data_array[q]) <7:
            has_data.append(joined_data_array[q])
        else:
            missing_data.append(joined_data_array[q])

    list_db=[]
    for q in joined_data_array:
        list_db.append(joined_data_array[q][0])
    list_db=set(list_db)

    list_evey_thing = []
    for q in joined_data_array:
        list_evey_thing.append(joined_data_array[q][2])







    return joined_data_array,has_data,list_db,db_data,list_evey_thing,missing_data


