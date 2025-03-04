def tinhtong_sochan(list):
    tong = 0
    for num in list:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

tong_chan = tinhtong_sochan(numbers)

print("Tổng các số chẵn trong danh sách là:", tong_chan)
