def daonguoclist(lst):
    return lst[::-1]

input_list = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int,input_list.split(',')))

list_daonguoc = daonguoclist(numbers)

print("Danh sách sau khi đảo ngược là:", list_daonguoc)