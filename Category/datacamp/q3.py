# 3
def common_data(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                print("True")


list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10]

common_data(list1, list2)
