sogiolam = float(input("Nhập số giờ làm: "))
luonggio = float(input("Nhập lương mỗi giờ: "))
giotieuchuan = 44
giovuotchuan = max(0, sogiolam - giotieuchuan)

luong = giotieuchuan * luonggio + giovuotchuan * luonggio * 1.5

print(f"Lương của bạn là: {luong}")