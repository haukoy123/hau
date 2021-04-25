            # FUNCTION

def func_exerc(*args):
    for i in args:
        print(i)


# func_exerc(20, 40, 25)


def func_exerc3(a, b):
    return a+b, a-b

# res = calculation(40, 10)
# print(res)
#
# # or
#
# add, sub = calculation(40, 10)
# print(add)
# print(sub)

def func_exerc6(num):
    # num !=0 -> true
    # num = 0-> false
    if num:
        # return num + calculateSum(num-1)
        return num + func_exerc6(num-1)
    else:
        return 0

# print(func_exerc6(10))





            # STRING

def string_exerc2(s1, s2):
    middleIndex = int(len(s1) / 2)
    print("Original Strings are", s1, s2)
    middleThree = s1[:middleIndex]+ s2 +s1[middleIndex:]
    print("After appending new string in middle", middleThree)

# string_exerc2("Ault", "Kelly")

def string_exerc3(s1, s2):
    middleIndex1 = int(len(s1)/2)
    middleIndex2 = int(len(s2)/2)

    result = s1[0] + s2[0] + s1[middleIndex1] + s2[middleIndex2] + s1[-1] + s2[-1]
    print(result)

# string_exerc3("america", "japan")


def string_exerc5(str):
    lowerCount = 0
    upperCount = 0
    digitCount = 0
    symbolCount = 0

    for char in str:
        if char.islower():
            lowerCount += 1
        elif char.isupper():
            upperCount += 1
        elif char.isdigit():
            digitCount += 1
        else:
            symbolCount += 1
    print("Lower case = ", lowerCount, "\nUpper case = ", upperCount, "\nDigits = ", digitCount, "\nSymbol = ", symbolCount)


# string_exerc5("P@#yn26at^&i5ve")

def string_exerc6(str1, str2):
    lengthstr1 = len(str1)
    lengthstr2 = len(str2)
    n = lengthstr1 if lengthstr1 > lengthstr2 else lengthstr2
    result = ""
    for i in range(n):
        if (i < lengthstr1):
            result = result + str1[i]
        if (i < lengthstr2):
            result = result + str2[i]
    print(result)


# string_exerc6("Abcdd", "Xyz")


def string_exerc8():
    inputString = "Welcome to USA. usa awesome, isn't it?"
    substring = "USA"

    # chuyen ve ki tu thuong
    tempString = inputString.lower()

    # chuyen chuoi tim kiem ve ki tu thuong
    # dem so lan xuat hien trong chuoi
    count = tempString.count(substring.lower())
    print("The USA count is:", count)
    print(substring)

# string_exerc8()



import re

#Split the string at every white-space character:
def string_exerc9():
    inputStr = "English = 1 Science = 2 Math = 3 History = 14"
    # r: tung chuoi nho; \b: bat dau chuoi; \d+: cac so den het chuoi; \b: kt chuoi
    x = re.findall(r'\b\d+\b', inputStr)
    markList = [int(num) for num in x]
    # or
    # for num in x:
    #     markList.append(int(num))
    totalMarks = 0
    for mark in markList:
        totalMarks += mark

    percentage = totalMarks / len(markList)
    print("Total Marks is:", totalMarks, "Percentage is ", percentage)
# string_exerc9()



                    # Data Structure#

def data_exerc1():
    listOne = [3, 6, 9, 12, 15, 18, 21]
    listTwo = [4, 8, 12, 16, 20, 24, 28]
    listThree = list()

    # list[(vtri bat da)::(buoc nhay)]
    oddElements = listOne[1::2]
    print("Element at odd-index positions from list one")
    print(oddElements)

    EvenElement = listTwo[0::2]
    print("Element at even-index positions from list two")
    print(EvenElement)

    print("Printing Final third list")
    listThree.extend(oddElements)
    listThree.extend(EvenElement)
    print(listThree)

# data_exerc1()


def data_exerc4():
    list_num = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    print(list_num)
    dict = {}
    # or
    # dict = dict()
    for i in list_num:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)

# data_exerc4()


def data_exerc5():
    list1 = [2, 3, 4, 5, 6, 7, 8]
    list2 = [4, 9, 16, 25, 36, 49, 64]
    list3 = set()
    for i in range(len(list1)):
        listn = (list1[i], list2[i])
        list3.add(listn)
    print(list3)
data_exerc5()


