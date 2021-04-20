import json


class Student:
    id = 0
    name = ""
    age = ""
    address = ""
    class_room = ""

    def __init__(self, idstd, namestd, agestd, addrstd, classstd):
        self.id = idstd
        self.name = namestd
        self.age = agestd
        self.address = addrstd
        self.class_room = classstd


data = {}
def new_dict(id2, name2, age2, address2, class2):
    # print(id2)
    dic_id2 = {
        'id': id2,
        'name': name2,
        'age': age2,
        'address': address2,
        'class': class2
    }
    # data[id22] = dic_id2
    return dic_id2

def add_new_dict(dict, new_id):
    key = str(new_id)
    data[key] = dict
    return data


def write_file():
    with open('qlsv.json', 'w') as outfile:
        json.dump(data, outfile)

def show():
    for p in data.keys():
      print(data[p])

def read_file():
    with open('qlsv.json') as json_file:
        global data
        data = json.load(json_file)
    return data

def nhap():

    print("id")
    global id

    id = int(input())
    print("Name")
    global name
    name = input()
    print("Age")
    global age
    age = input()
    print("class")
    global class_room
    class_room = input()
    print("Address")
    global address
    address = input()

def insert():
    nhap()
    read_file()
    add_new_dict(new_dict(id, name, age, address, class_room), id)
    write_file()
    read_file()
    for p in data.keys():
        print(data[p])

def update():
    nhap()
    read_file()
    # for p in data.keys():
    #     print(data[p])
    id2 = str(id)
    if id2 in data.keys():
        data.update({id2: new_dict(id, name, age, address, class_room)})
        # data[id2] = new_dict(id, name, age, address, class_room)
        write_file()
        read_file()
        show()
        # data[id22] = dic_id2
    else:
        print("not found")


def delete():
    read_file()
    id1 = str(input("ID to delete: "))
    if id1 in data.keys():
        del data[id1]
        write_file()
    else:
        print("not found")
    read_file()
    show()


def student_addr():
    read_file()
    address1 = str(input("Address student: "))
    for p in data.keys():
        if address1 == data[p]["address"]:
            print(data[p])





# insert()
# write_file()
read_file()
# update()
# delete()
# student_addr()