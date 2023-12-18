from utils.encrypt import MDAEncrypt


class MDAForm:

    def __init__(self):
        self.hidden_mda_opt()
        self.mda_mod_combo.activated.connect(self.mda_encrypt)
        self.mda_input.textChanged.connect(self.mda_encrypt)
        self.mda_salt.textChanged.connect(self.mda_encrypt)
        self.mda_format_combo.activated.connect(self.mda_encrypt)

    def show_mda_opt(self):
        self.label_mda_salt.setVisible(True)
        self.mda_salt.setVisible(True)
        self.mda_format_combo.setVisible(True)
        self.label_mda_format.setVisible(True)

    def hidden_mda_opt(self):
        self.label_mda_salt.setVisible(False)
        self.mda_salt.setVisible(False)
        self.mda_format_combo.setVisible(False)
        self.label_mda_format.setVisible(False)
        self.mda_salt.setText("")

    def mda_encrypt(self):
        salt = ""
        mda_type = self.mda_mod_combo.currentText()
        if "HMAC-" in mda_type:
            self.show_mda_opt()
            salt = self.mda_salt.text()
            if not salt:
                self.mda_output.setPlainText("")
                return
        else:
            self.hidden_mda_opt()
        plain_text = self.mda_input.toPlainText()
        if not plain_text:
            return
        encrypt_text = MDAEncrypt.encrypt(mda_type, plain_text, salt, self.mda_format_combo.currentIndex())
        self.mda_output.setPlainText(encrypt_text)
