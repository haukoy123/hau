def exercise_1():
    a = int(input("number1 = "))
    b = int(input("number2 =  "))
    mul = a * b
    if mul > 1000:
        return a + b
    else:
        return a * b


def exercise_2():
    prv = 0
    for i in range(10):
        sum = i + prv
        print("Current Number {} Previous Number  {}  Sum: {}".format(i, prv, sum))
        prv = i


def exercise_3():
    chuoi = input("Nhap chuoi: ")
    for i in range(len(chuoi)):
        if i % 2 == 0:
            print(chuoi[i])


def exercise_4():
    chuoi = input("Nhap chuoi: ")
    n = int(input("So ky tu dau can xoa: "))

    print("chuoi: ", chuoi[n:])


def exercise_5():
    list_num = []
    print("Nhap 5 so")
    for i in range(5):
        print("So", i+1, ":")
        num = int(input())
        list_num.append(num)
    if list_num[0] == list_num[-1]:
        return True
    else:
        return False

def exercise_6():
    list_num = []
    print("Nhap 5 so")
    for i in range(5):
        print("So", i + 1, ":")
        num = int(input())
        list_num.append(num)
    print("Danh sach so:", list_num)
    print("So chia het cho 5:")
    for p in range(len(list_num)):
        if list_num[p] % 5 == 0:
            print(list_num[p])

#
# def exercise_7():
#     chuoi1 = input("chuoi: ")
#     chuoi2 = input("chuoi kiem tra: ")
#


# exercise_6()
# print(exercise_5())
# exercise_4()
# print("The result is ", exercise_1())
# exercise_2()
# exercise_3()