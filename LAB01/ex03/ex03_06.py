def xoaphantu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
result = xoaphantu(my_dict, key_to_delete)
if result:
    print("Phần tử đã được xoá từ Dictionary:", my_dict)
else:
    print("Không tìm thấy phần tử trong Dictionary")