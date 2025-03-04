def demsolanxuathien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_str = (input("Nhập danh sách các từ, cách nhau bởi dấu cách: "))
word_list = input_str.split()

solanxuathien = demsolanxuathien(word_list)

print("Số lần xuất hiện của mỗi từ trong danh sách là:", solanxuathien)