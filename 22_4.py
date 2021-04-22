# Input and Output

def exerc2():
    print("My","name", "is", "Hau", sep="**")

# exerc2()

def exerc3():
    print('%o,' % (8))
# exerc3()


def exerc4():
    print('%.2f' % 3.335333)

# exerc4()


def exerc5():
    list = []
    n = int(input("so phan tu:"))
    for i in range(n):
        print("so ", i+1)
        a = float(input())
        list.append(a)
    print(list)

# exerc5()

#
# def exerc6():
#     count = 0
#     with open("exerc6.txt", "r") as file:
#         # doc theo tung dong
#         lines = file.readlines()
#         count = len(lines)
#     with open("newfile.txt", "w") as file1:
#         for line in lines:
#             if count == 4:
#                 continue
#             else:
#                 file1.write(line)
#                 print(line)
#         # print(lines[4])
#
# exerc6()



def exerc7():
    str1, str2, str3 = input("Enter three string: ").split()
    print(str1, str2, str3)

# exerc7()



#   loop

def loop_exerc_2():
    n = 5
    for i in range(1, n+1):
        for m in range(1, i+1):
            # end("*") cung dong cach nhau boi *
            print(m, end=("  "))
        print("")

# loop_exerc_2()

def loop_exerc_4():
    n = 2
    for i in range(1, 11):
        print(n*i)

# loop_exerc_4()
def loop_exerc_5():
    list_num = []
    print("Nhap 5 so")
    for i in range(5):
        print("So", i + 1, ":")
        num = int(input())
        list_num.append(num)
    print("Danh sach so:", list_num)
    print("So chia het cho 5 duoi 150:")
    for p in list_num:
        if p > 150:
            break
        else:
            if p % 5 == 0:
                print(p)

# loop_exerc_5()

def loop_exerc_7():
    for i in range(0, 5):
        # range(start, stop, step): step = -n quay lại 1 khoảng n
        for m in range(5-i, 0, -1):
            print(m, end=("  "))
        print("")
# loop_exerc_7()


def loop_exerc_8():
    a = int(input("start number: "))
    b = int(input("end number: "))
    m = 0
    for num in range(a, b+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    m = 0
                    break
                else:
                    m = i
            if m != 0:
                print(num)
loop_exerc_8()




