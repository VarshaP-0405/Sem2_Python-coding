##1##
def Merge_dict(d1, d2):
    d1.update(d2)  
    print(d1)

D1 = {"VARSHA": 99, "VASUDHA": 88}
D2 = {"PRASADH": 77, "BARGAVI": 66}
Merge_dict(D1, D2)
##2##
def count_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    result = {}
    for elem in common_elements:
        result[elem] = min(list1.count(elem), list2.count(elem))  
    return result


list1 = list(map(int,input("ENTER VALUES FOR LIST 1:").split())
list2 = list(map(int,input("ENTER VALUES FOR LIST 2:").split())
result = count_common_elements(list1, list2)
print(result)
##3##
def list_to_dict():
    n = int(input("Enter the number of key-value pairs: "))
    tuples_list = []
    for _ in range(n):
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        tuples_list.append((key, value))
    return dict(tuples_list)
result = list_to_dict()
print("Converted Dictionary:", result)
