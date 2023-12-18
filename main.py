import sys
from PyQt5.QtWidgets import QWidget, QApplication
from ui.encrypt_ui import Ui_EncryptForm
from form import MDAForm, SymmetricForm, HeadersForm, AsymmetricForm, RailFenceCipherForm, MsgQueueForm


class MyWindow(QWidget, Ui_EncryptForm, MDAForm, SymmetricForm,
               AsymmetricForm, RailFenceCipherForm, HeadersForm, MsgQueueForm):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        MDAForm.__init__(self)
        SymmetricForm.__init__(self)
        AsymmetricForm.__init__(self)
        RailFenceCipherForm.__init__(self)
        HeadersForm.__init__(self)
        MsgQueueForm.__init__(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
