from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while(1==1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("------------------MENU------------------")
    print("1. Thêm sinh viên")
    print("2. Sửa thông tin sinh viên")
    print("3. Xóa sinh viên theo ID")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm trung bình")
    print("6. Sắp xếp sinh viên theo chuyên ngành")
    print("7. Hiển thị danh sách sinh viên")
    print("8. Thoát")
    print("----------------------------------------")

    key = int(input("Nhập lựa chọn của bạn: "))
    if(key == 1):
        print("\n 1. Thêm sinh viên")
        qlsv.nhapSinhVien()
        print("\nThêm sinh viên thành công !")
    elif(key == 2):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 2. Sửa thông tin sinh viên")
            print("\nNhập ID:")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sách sinh viên rỗng !")
    elif(key == 3):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 3. Xóa sinh viên theo ID")
            print("\nNhập ID:")
            ID = int(input())
            if(qlsv.deleteById(ID)):
                print("\nSinh viên có id = ",ID," đã bị xóa !")
            else:
                print("\nKhông tìm thấy sinh viên có id = ",ID)
        else:
            print("\nDanh sách sinh viên rỗng !")
    elif(key == 4):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 4. Tìm kiếm sinh viên theo tên")
            print("\nNhập tên sinh viên:")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sách sinh viên rỗng !")
    elif(key == 5):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 5. Sắp xếp sinh viên theo điểm trung bình")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhvien())
        else:
            print("\nDanh sách sinh viên rỗng !")
    elif(key == 6):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 6. Sắp xếp sinh viên theo tên")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhvien())
        else:
            print("\nDanh sách sinh viên rỗng !")
    elif(key == 7):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n 7. Hiển thị danh sách sinh viên")
            qlsv.showSinhVien(qlsv.getListSinhvien())
        else:
            print("\nDanh sách sinh viên rỗng !")
    elif(key == 0):
        print("\n Bạn đã chọn thoát chương trình!")
        break
    else:
        print("\nLựa chọn không hợp lệ, vui lòng chọn lại!")

           