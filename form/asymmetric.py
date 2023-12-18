from utils.encrypt import RSAEncrypt
from PyQt5.QtWidgets import QMessageBox


class AsymmetricForm:

    def __init__(self):
        self.asymmetric_generate.clicked.connect(self.generate_key_pairs)
        self.asymmetric_encrypt.clicked.connect(self.asymme_encrypt)
        self.asymmetric_decrypt.clicked.connect(self.asymme_decrypt)

    def generate_key_pairs(self):
        public_key, private_key = RSAEncrypt.generate_key_pairs(int(self.asymmetric_key_length_combo.currentText()))
        self.public_key.setPlainText(public_key.decode())
        self.private_key.setPlainText(private_key.decode())

    def asymme_encrypt(self):
        try:
            text = self.asymmetric_plaintext.toPlainText()
            cipher_text = RSAEncrypt.encrypt(self.public_key.toPlainText(), text)
            self.asymmetric_ciphertext.setPlainText(cipher_text)
        except Exception as e:
            QMessageBox.about(self, "错误", str(e))

    def asymme_decrypt(self):
        try:
            text = self.asymmetric_ciphertext.toPlainText()
            plain_text = RSAEncrypt.decrypt(self.private_key.toPlainText(), text)
            self.asymmetric_plaintext.setPlainText(plain_text)
        except Exception as e:
            QMessageBox.about(self, "错误", str(e))
