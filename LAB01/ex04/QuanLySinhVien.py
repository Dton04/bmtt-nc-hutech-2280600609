from Sinhvien import Sinhvien

class QuanLySinhVien:
    listSinhvien = []

    def generateID(self):
        maxId = 1
        if(self.soLuongSinhVien() > 0 ):
            maxId = self.listSinhvien[0]._id
            for sv in self.listSinhvien:
                if(maxId < sv._id):
                    maxId = sv._id
            maxId += 1
        return maxId
    def soLuongSinhVien(self):
        return self.listSinhvien.__len__()
    
    def nhapSinhVien(self):
        id = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính: ")
        major = input("Nhập ngành học: ")
        diemTB = float(input("Nhập điểm trung bình: "))
        sv = Sinhvien(id, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhvien.append(sv)

    def updateSinhVien(self,ID):
        sv:Sinhvien = self.findByID(ID)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính: ")
            major = input("Nhập ngành học: ")
            diemTB = float(input("Nhập điểm trung bình: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Không tìm thấy sinh viên có ID: ",ID)
    
    def sortByID(self):
        self.listSinhvien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhvien.sort(key=lambda x: x._name, reverse=False)
    
    def sortByDiemTB(self):
        self.listSinhvien.sort(key=lambda x: x._diemTB, reverse=False)
    
    def findByID(self,ID):
        searchResult = None
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhvien:
                if(sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhvien:
                if(keyword in sv._name):
                    listSV.append(sv)
        return listSV
    
    def deleteById(self,ID):
        isDeleted = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhvien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:Sinhvien):
        if(sv._diemTB >= 8):
            sv._hocLuc = "Giỏi"
        elif(sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif(sv._diemTB >= 5):
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"
    
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:8} {:<8}{:<8} {:<8}"
              .format("ID", "Tên sinh viên", "Giới tính", "Ngành học", "Điểm TB", "Học lực"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:8} {:<8}{:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex , sv._major, sv._diemTB, sv._hocLuc))
                print("\n")
    def getListSinhVien(self):
        return self.listSinhvien 