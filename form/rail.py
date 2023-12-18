from utils.encrypt import RailFenceCipher
from PyQt5.QtWidgets import QMessageBox


class RailFenceCipherForm:

    def __init__(self):
        self.rail_encrypt.clicked.connect(self.rail_fence_encrypt)
        self.rail_decrypt.clicked.connect(self.rail_fence_decrypt)

    def get_cipher(self):
        fence_num = self.rail_fence_num.text()
        rail_space = self.rail_space.text()
        if not fence_num.isdigit() or int(fence_num) < 2:
            QMessageBox.about(self, "提示", "栏数必须为2以上")
            return
        return RailFenceCipher(fence_num, rail_space)

    def rail_fence_encrypt(self):
        cipher = self.get_cipher()
        if cipher:
            cipher_text = cipher.encrypt(self.rail_plaintext.toPlainText())
            self.rail_ciphertext.setPlainText(cipher_text)

    def rail_fence_decrypt(self):
        cipher = self.get_cipher()
        if cipher:
            plain_text = cipher.decrypt(self.rail_ciphertext.toPlainText())
            self.rail_plaintext.setPlainText(plain_text)
