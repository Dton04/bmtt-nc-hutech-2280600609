class RailFenceCipher:
    def rail_fence_encrypt(self, plain_text, key):
        # Tạo bảng zigzag
        rail = [['\n' for _ in range(len(plain_text))] for _ in range(key)]
        dir_down = False
        row, col = 0, 0

        # Điền dữ liệu vào bảng zigzag
        for char in plain_text:
            if row == 0 or row == key - 1:
                dir_down = not dir_down
            rail[row][col] = char
            col += 1
            row += 1 if dir_down else -1

        # Đọc dữ liệu từ bảng zigzag
        encrypted_text = []
        for i in range(key):
            for j in range(len(plain_text)):
                if rail[i][j] != '\n':
                    encrypted_text.append(rail[i][j])
        return ''.join(encrypted_text)

    def rail_fence_decrypt(self, cipher_text, key):
        # Tạo bảng zigzag
        rail = [['\n' for _ in range(len(cipher_text))] for _ in range(key)]
        dir_down = None
        row, col = 0, 0

        # Đánh dấu vị trí zigzag
        for _ in range(len(cipher_text)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
            rail[row][col] = '*'
            col += 1
            row += 1 if dir_down else -1

        # Điền dữ liệu vào bảng zigzag
        index = 0
        for i in range(key):
            for j in range(len(cipher_text)):
                if rail[i][j] == '*' and index < len(cipher_text):
                    rail[i][j] = cipher_text[index]
                    index += 1

        # Đọc dữ liệu từ bảng zigzag
        result = []
        row, col = 0, 0
        for _ in range(len(cipher_text)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
            if rail[row][col] != '\n':
                result.append(rail[row][col])
                col += 1
            row += 1 if dir_down else -1
        return ''.join(result)