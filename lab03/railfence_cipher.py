import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        payload = {
            "plain_text": self.ui.txt_plaintext.toPlainText(),
            "key": self.ui.txt_key.text()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if "encrypted_text" in data:  # Sửa lại khóa
                    self.ui.txt_ciphertext.setText(data["encrypted_text"])
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Mã hóa thành công!")
                    msg.exec_()
                else:
                    print("Không tìm thấy khóa 'encrypted_text' trong phản hồi:", data)
                    QMessageBox.critical(self, "Lỗi", "Định dạng phản hồi API không hợp lệ.")
            else:
                print("Lỗi khi gọi API:", response.text)
                QMessageBox.critical(self, "Lỗi", f"Lỗi API: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("Lỗi: %s" % e)
            QMessageBox.critical(self, "Lỗi", f"Yêu cầu thất bại: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        payload = {
            "cipher_text": self.ui.txt_ciphertext.toPlainText(),
            "key": self.ui.txt_key.text()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if "decrypted_text" in data:  # Sửa lại khóa
                    self.ui.txt_plaintext.setText(data["decrypted_text"])
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Giải mã thành công!")
                    msg.exec_()
                else:
                    print("Không tìm thấy khóa 'decrypted_text' trong phản hồi:", data)
                    QMessageBox.critical(self, "Lỗi", "Định dạng phản hồi API không hợp lệ.")
            else:
                print("Lỗi khi gọi API:", response.text)
                QMessageBox.critical(self, "Lỗi", f"Lỗi API: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("Lỗi: %s" % e)
            QMessageBox.critical(self, "Lỗi", f"Yêu cầu thất bại: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())