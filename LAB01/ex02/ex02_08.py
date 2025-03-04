def chia_het_cho_5(sonhiphan):
    sothapphan = int(sonhiphan, 2)

    if sothapphan % 5 == 0:
        return True
    else:
        return False

chuoi_sonhiphan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")
sonhiphan_list = chuoi_sonhiphan.split(", ")
so_chia_het_cho_5 = [so for so in sonhiphan_list if chia_het_cho_5(so)]

if len(so_chia_het_cho_5) > 0:
    ketqua = ",".join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là:",ketqua)
else:
    print("Không có số nhị phân nào chia hết cho 5.")