from PyQt5.QtWidgets import QMessageBox
from utils.encrypt import SymmetricEncryption


class SymmetricForm:

    def __init__(self):
        self.set_visible_ecb_opt(False)
        self.symmetric_model_combo.activated.connect(self.model_combo_signal)
        self.symmetric_mod_combo.activated.connect(self.mod_combo_signal)
        self.encryption_btn.clicked.connect(self.symmetric_encrypt)
        self.decrypt_btn.clicked.connect(self.symmetric_decrypt)

    def set_visible_ecb_opt(self, b):
        self.symmetric_iv.setVisible(b)
        self.label_symmetric_iv.setVisible(b)

    def set_visible_des_opt(self, b):
        self.label_symmetric_key_length.setVisible(b)
        self.symmetric_key_length_combo.setVisible(b)

    def set_visible_rc4_opt(self, b):
        self.label_symmetric_mod.setVisible(b)
        self.symmetric_mod_combo.setVisible(b)
        self.label_symmetric_fill.setVisible(b)
        self.symmetric_fill_combo.setVisible(b)
        self.label_symmetric_key_length.setVisible(b)
        self.symmetric_key_length_combo.setVisible(b)
        self.label_symmetric_format.setVisible(b)
        self.symmetric_format_combo.setVisible(b)
        self.label_symmetric_iv.setVisible(b)
        self.symmetric_iv.setVisible(b)

    def resetting(self):
        self.symmetric_key.setMaxLength(32767)
        self.symmetric_iv.setMaxLength(32767)
        self.set_visible_des_opt(True)
        self.set_visible_rc4_opt(True)

    def model_combo_signal(self):
        current_text = self.symmetric_model_combo.currentText()
        self.resetting()
        self.mod_combo_signal()
        if "DES" in current_text:
            self.set_visible_des_opt(False)
        if current_text == "DES":
            self.symmetric_key.setMaxLength(8)
            self.symmetric_iv.setMaxLength(8)
        elif current_text == "3DES":
            self.symmetric_key.setMaxLength(24)
            self.symmetric_iv.setMaxLength(8)
        elif current_text == "RC4":
            self.set_visible_rc4_opt(False)

    def mod_combo_signal(self):
        if self.symmetric_mod_combo.currentText() != "ECB":
            self.set_visible_ecb_opt(True)
        else:
            self.set_visible_ecb_opt(False)
            self.symmetric_iv.setText("")

    def get_symmetric_dto(self):
        symmetric_type = self.symmetric_model_combo.currentText()
        mode = self.symmetric_mod_combo.currentText()
        key = self.symmetric_key.text()
        length = int(self.symmetric_key_length_combo.currentText()) if symmetric_type == "AES" else 8
        iv = self.symmetric_iv.text()
        fill = self.symmetric_fill_combo.currentText()
        b64 = self.symmetric_format_combo.currentIndex()
        return SymmetricEncryption(symmetric_type, mode, key, length, iv, fill, b64)

    def push_verify(self):
        if self.symmetric_model_combo.currentText() == "DES":
            if len(self.symmetric_key.text()) != 8:
                QMessageBox.about(self, "提示", "密钥必须为8位")
                return
            elif self.symmetric_iv.isVisible() and len(self.symmetric_iv.text()) != 8:
                QMessageBox.about(self, "提示", "向量必须为8位")
                return
        elif self.symmetric_model_combo.currentText() == "3DES":
            key_len = len(self.symmetric_key.text())
            if key_len != 16 and key_len != 24:
                QMessageBox.about(self, "提示", "密钥必须为16或24位")
                return
            elif self.symmetric_iv.isVisible() and len(self.symmetric_iv.text()) != 8:
                QMessageBox.about(self, "提示", "向量必须为8位")
                return
        return True

    def symmetric_encrypt(self):
        if not self.push_verify():
            return
        try:
            s = self.get_symmetric_dto()
            plaintext = self.symmetric_plaintext.toPlainText()
            cipher_text = s.encrypt(plaintext)
            self.symmetric_ciphertext.setPlainText(cipher_text)
        except Exception as exc:
            QMessageBox.about(self, "Error", str(exc))

    def symmetric_decrypt(self):
        if not self.push_verify():
            return
        try:
            s = self.get_symmetric_dto()
            cipher_text = self.symmetric_ciphertext.toPlainText()
            plaintext = s.decrypt(cipher_text)
            self.symmetric_plaintext.setPlainText(plaintext)
        except Exception as exc:
            QMessageBox.about(self, "Error", str(exc))
