class RailFenceCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        # Tạo các hàng cho Rail Fence
        rail = [['\n' for _ in range(len(text))] for _ in range(key)]
        direction_down = False
        row, col = 0, 0

        # Điền các ký tự vào Rail Fence
        for char in text:
            if row == 0 or row == key - 1:
                direction_down = not direction_down
            rail[row][col] = char
            col += 1
            row += 1 if direction_down else -1

        # Đọc các ký tự theo thứ tự hàng
        encrypted_text = ''.join([''.join(row) for row in rail if row])
        return encrypted_text

    def decrypt(self, cipher_text, key):
        # Tạo các hàng cho Rail Fence
        rail = [['\n' for _ in range(len(cipher_text))] for _ in range(key)]
        direction_down = None
        row, col = 0, 0

        # Đánh dấu vị trí các ký tự
        for _ in cipher_text:
            if row == 0 or row == key - 1:
                direction_down = not direction_down
            rail[row][col] = '*'
            col += 1
            row += 1 if direction_down else -1

        # Điền các ký tự vào Rail Fence
        index = 0
        for i in range(key):
            for j in range(len(cipher_text)):
                if rail[i][j] == '*' and index < len(cipher_text):
                    rail[i][j] = cipher_text[index]
                    index += 1

        # Đọc các ký tự theo thứ tự zigzag
        result = []
        row, col = 0, 0
        for _ in cipher_text:
            if row == 0 or row == key - 1:
                direction_down = not direction_down
            if rail[row][col] != '*':
                result.append(rail[row][col])
                col += 1
            row += 1 if direction_down else -1

        return ''.join(result)