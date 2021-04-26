                    # Data Structure#
def data_exerc6():
    set1 = {23, 42, 65, 57, 78, 83, 29}
    set2 = {57, 83, 29, 67, 73, 43, 48}
    set3 = set1.intersection(set2)
    for i in set3:
        set1.remove(i)
    print("set1 after removing common element:", set1)
    print("Intersection:",set3)
# data_exerc6()

                    # list

def list_exerc1():
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    list3=[]
    for i, j in zip(list1, list2):
        list3.append(i+j)
    print(list3)

# list_exerc1()

def list_exerc4():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    list3 = []
    for i in list1:
        for j in list2:
            list3.append(i+j)

    print(list3)

# list_exerc4()

def list_exerc5():
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]

    # set1 = zip(list1,list2[::-1])
    # list3 = list(set1)
    # print(list3)
    for i, j in zip(list1, list2[::-1]):
        print(i, j)

# list_exerc5()

def list_exerc6():
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    list2 = list(filter(None, list1))
    print(list2)

# list_exerc6()
def list_exerc7():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list1[2][2].append(7000)
    print(list1)

# list_exerc7()

def list_exerc8():
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    list2 = ["h", "i", "j"]
    list1[2][1][2].extend(list2)
    print(list1)

# list_exerc8()


                    # Dictionary

def dict_exerc1():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    dict1 = {}
    for i, j in zip(keys, values):
        dict1[i] = j
    # or
    # dict1 = dict(zip(keys, values))
    print(dict1)

# dict_exerc1()

def dict_exerc2():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    for i in dict2:
        dict1[i] = dict2[i]
    # or
    # dict3 = {**dict1, **dict2}(gop dict1 và dict2, trung dict2  ghi de
    print(dict1)
# dict_exerc2()

def dict_exerc4():
    employees = ['Kelly', 'Emma', 'John']
    defaults = {"designation": 'Application Developer', "salary": 8000}

    # fromkeys(key, value): tạo mot dict voi bo key và bo value cho trc
    resDict = dict.fromkeys(employees, defaults)
    print(resDict)

    print(resDict["Kelly"])

# dict_exerc4()
def dict_exerc5():
    sampleDict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    newdict = {}
    keys = ["name", "salary"]
    for i in keys:
        newdict[i] = sampleDict[i]

    print(newdict)

# dict_exerc5()
def dict_exerc6():
    sampleDict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    keys = ["name", "salary"]
    for i in keys:
        del sampleDict[i]
    print(sampleDict)

# dict_exerc6()



                        # set


def set_exerc1():
    sampleSet = {"Yellow", "Orange", "Black"}
    sampleList = ["Blue", "Green", "Red"]
    sampleSet.update(sampleList)
    print(sampleSet)
# set_exerc1()

def set_exerc2():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set3 = set()
    for i in set1:
        for j in set2:
            if i == j:
                set3.add(i)
    # or
    # set3 = set1.intersection(set2)
    print(set3)

# set_exerc2()


def set_exerc3():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    # intersection(): lay giao, union(): lay khong giao
    set3 = set1.union(set2)
    print(set3)

# set_exerc3()


def set_exerc4():
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}
    set1.difference_update(set2)
    print(set1)

# set_exerc4()



                        # Tuple

def tuple_exerc2():
    aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
    print(aTuple[1][1])
# tuple_exerc2()


def tuple_exerc4():
    aTuple = (10, 20, 30, 40)
    for i in aTuple:
        print(i)

# tuple_exerc4()

def tuple_exerc6():
    tuple1 = (11, 22, 33, 44, 55, 66)
    tuple2 = tuple1[3:5]
    print(tuple2)

# tuple_exerc6()

def tuple_exerc8():
    tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
    tuple2 = tuple(sorted(tuple1, key=lambda a: a[1]))
    print(tuple2)

# tuple_exerc8()



                    #  Date and Time
from datetime import datetime, timedelta
import time
def dt_exerc1():
    print(datetime.now())
    print(datetime.now().date())
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# dt_exerc1()

def dt_exerc2():
    date_string = "Feb 25 2020  4:20PM"
    datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
    print(datetime_object)

# dt_exerc2()


def dt_exerc3():
    given_date = datetime(2020, 2, 25)
    result = given_date - timedelta(7)
    print(result)
# dt_exerc3()

def dt_exerc4():
    given_date = datetime(2020, 2, 25)
    result = datetime.strftime(given_date, "%A %d %B %Y")
    print(result)
# dt_exerc4()


def dt_exerc6():
    given_date = datetime(2020, 3, 22, 10, 0, 0)
    result = given_date + timedelta(days=7, hours=12)
    print(result)
# dt_exerc6()


from dateutil.relativedelta import relativedelta

def dt_exerc9():
    given_date = datetime(2020, 2, 25).date()
    new_date = given_date + relativedelta(months=4)
    print(new_date)

# dt_exerc9()


def dt_exerc10():
    # 2020-02-25
    date_1 = datetime(2020, 2, 25)

    # 2020-09-17
    date_2 = datetime(2020, 9, 17)

    date = date_2-date_1
    print(date.days, "days")
# dt_exerc10()


