
from students import show, delete, insert, update, student_addr


def menu():
    print("1: Show list.")
    print("2: Add student.")
    print("3: Update student.")
    print("4: Delete student.")
    print("5: Student statistics by address.")

def run_funcion():
    x = int(input("Choose: "))
    switcher = {
        1: show,
        2: insert,
        3: update,
        4: delete,
        5: student_addr
    }
    if x not in switcher:
        raise Exception("not found")
    switcher[x]()

def repeat_menu():
    menu()
    ctn = input("Enter 'Yes' to continue: ")
    while ctn == "Yes":
        menu()
        run_funcion()
        ctn = input("Enter 'Yes' to continue: ")
    else:
        exit()

repeat_menu()






#
# def menu(x):
#     switcher = {
#         1: ,
#         # '2': update()
#         # 'delete':
#         4: stt
#     }
#     if x not in switcher:
#         raise Exception("not found")
#     return switcher[x]


