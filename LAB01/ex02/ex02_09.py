def  kiemtra_SNT(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Nhập số cần kiểm tra: "))
if kiemtra_SNT(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải là số nguyên tố.")