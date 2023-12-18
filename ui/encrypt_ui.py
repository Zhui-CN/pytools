# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encrypt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EncryptForm(object):
    def setupUi(self, EncryptForm):
        EncryptForm.setObjectName("EncryptForm")
        EncryptForm.resize(690, 612)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(EncryptForm)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(EncryptForm)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_mda = QtWidgets.QWidget()
        self.tab_mda.setObjectName("tab_mda")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_mda)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.label_mda_mod = QtWidgets.QLabel(self.tab_mda)
        self.label_mda_mod.setObjectName("label_mda_mod")
        self.horizontalLayout_1.addWidget(self.label_mda_mod)
        self.mda_mod_combo = QtWidgets.QComboBox(self.tab_mda)
        self.mda_mod_combo.setPlaceholderText("")
        self.mda_mod_combo.setObjectName("mda_mod_combo")
        self.mda_mod_combo.addItem("")
        self.mda_mod_combo.addItem("")
        self.mda_mod_combo.addItem("")
        self.mda_mod_combo.addItem("")
        self.mda_mod_combo.addItem("")
        self.mda_mod_combo.addItem("")
        self.mda_mod_combo.addItem("")
        self.mda_mod_combo.addItem("")
        self.mda_mod_combo.addItem("")
        self.mda_mod_combo.addItem("")
        self.mda_mod_combo.addItem("")
        self.mda_mod_combo.addItem("")
        self.horizontalLayout_1.addWidget(self.mda_mod_combo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem)
        self.label_mda_salt = QtWidgets.QLabel(self.tab_mda)
        self.label_mda_salt.setStyleSheet("")
        self.label_mda_salt.setObjectName("label_mda_salt")
        self.horizontalLayout_1.addWidget(self.label_mda_salt)
        self.mda_salt = QtWidgets.QLineEdit(self.tab_mda)
        self.mda_salt.setObjectName("mda_salt")
        self.horizontalLayout_1.addWidget(self.mda_salt)
        self.label_mda_format = QtWidgets.QLabel(self.tab_mda)
        self.label_mda_format.setObjectName("label_mda_format")
        self.horizontalLayout_1.addWidget(self.label_mda_format)
        self.mda_format_combo = QtWidgets.QComboBox(self.tab_mda)
        self.mda_format_combo.setObjectName("mda_format_combo")
        self.mda_format_combo.addItem("")
        self.mda_format_combo.addItem("")
        self.horizontalLayout_1.addWidget(self.mda_format_combo)
        self.verticalLayout_1.addLayout(self.horizontalLayout_1)
        self.mda_input = QtWidgets.QPlainTextEdit(self.tab_mda)
        self.mda_input.setObjectName("mda_input")
        self.verticalLayout_1.addWidget(self.mda_input)
        self.mda_output = QtWidgets.QTextBrowser(self.tab_mda)
        self.mda_output.setObjectName("mda_output")
        self.verticalLayout_1.addWidget(self.mda_output)
        self.horizontalLayout_7.addLayout(self.verticalLayout_1)
        self.tabWidget.addTab(self.tab_mda, "")
        self.tab_symmetric = QtWidgets.QWidget()
        self.tab_symmetric.setObjectName("tab_symmetric")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_symmetric)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_symmetric_model = QtWidgets.QLabel(self.tab_symmetric)
        self.label_symmetric_model.setObjectName("label_symmetric_model")
        self.horizontalLayout_3.addWidget(self.label_symmetric_model)
        self.symmetric_model_combo = QtWidgets.QComboBox(self.tab_symmetric)
        self.symmetric_model_combo.setObjectName("symmetric_model_combo")
        self.symmetric_model_combo.addItem("")
        self.symmetric_model_combo.addItem("")
        self.symmetric_model_combo.addItem("")
        self.symmetric_model_combo.addItem("")
        self.horizontalLayout_3.addWidget(self.symmetric_model_combo)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_symmetric_mod = QtWidgets.QLabel(self.tab_symmetric)
        self.label_symmetric_mod.setObjectName("label_symmetric_mod")
        self.horizontalLayout_3.addWidget(self.label_symmetric_mod)
        self.symmetric_mod_combo = QtWidgets.QComboBox(self.tab_symmetric)
        self.symmetric_mod_combo.setObjectName("symmetric_mod_combo")
        self.symmetric_mod_combo.addItem("")
        self.symmetric_mod_combo.addItem("")
        self.symmetric_mod_combo.addItem("")
        self.symmetric_mod_combo.addItem("")
        self.symmetric_mod_combo.addItem("")
        self.horizontalLayout_3.addWidget(self.symmetric_mod_combo)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_symmetric_fill = QtWidgets.QLabel(self.tab_symmetric)
        self.label_symmetric_fill.setObjectName("label_symmetric_fill")
        self.horizontalLayout_3.addWidget(self.label_symmetric_fill)
        self.symmetric_fill_combo = QtWidgets.QComboBox(self.tab_symmetric)
        self.symmetric_fill_combo.setObjectName("symmetric_fill_combo")
        self.symmetric_fill_combo.addItem("")
        self.symmetric_fill_combo.addItem("")
        self.symmetric_fill_combo.addItem("")
        self.horizontalLayout_3.addWidget(self.symmetric_fill_combo)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_symmetric_key_length = QtWidgets.QLabel(self.tab_symmetric)
        self.label_symmetric_key_length.setObjectName("label_symmetric_key_length")
        self.horizontalLayout_3.addWidget(self.label_symmetric_key_length)
        self.symmetric_key_length_combo = QtWidgets.QComboBox(self.tab_symmetric)
        self.symmetric_key_length_combo.setObjectName("symmetric_key_length_combo")
        self.symmetric_key_length_combo.addItem("")
        self.symmetric_key_length_combo.addItem("")
        self.symmetric_key_length_combo.addItem("")
        self.horizontalLayout_3.addWidget(self.symmetric_key_length_combo)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_symmetric_format = QtWidgets.QLabel(self.tab_symmetric)
        self.label_symmetric_format.setObjectName("label_symmetric_format")
        self.horizontalLayout_3.addWidget(self.label_symmetric_format)
        self.symmetric_format_combo = QtWidgets.QComboBox(self.tab_symmetric)
        self.symmetric_format_combo.setObjectName("symmetric_format_combo")
        self.symmetric_format_combo.addItem("")
        self.symmetric_format_combo.addItem("")
        self.horizontalLayout_3.addWidget(self.symmetric_format_combo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_symmetric_key = QtWidgets.QLabel(self.tab_symmetric)
        self.label_symmetric_key.setObjectName("label_symmetric_key")
        self.horizontalLayout_2.addWidget(self.label_symmetric_key)
        self.symmetric_key = QtWidgets.QLineEdit(self.tab_symmetric)
        self.symmetric_key.setObjectName("symmetric_key")
        self.horizontalLayout_2.addWidget(self.symmetric_key)
        self.label_symmetric_iv = QtWidgets.QLabel(self.tab_symmetric)
        self.label_symmetric_iv.setObjectName("label_symmetric_iv")
        self.horizontalLayout_2.addWidget(self.label_symmetric_iv)
        self.symmetric_iv = QtWidgets.QLineEdit(self.tab_symmetric)
        self.symmetric_iv.setObjectName("symmetric_iv")
        self.horizontalLayout_2.addWidget(self.symmetric_iv)
        self.encryption_btn = QtWidgets.QPushButton(self.tab_symmetric)
        self.encryption_btn.setObjectName("encryption_btn")
        self.horizontalLayout_2.addWidget(self.encryption_btn)
        self.decrypt_btn = QtWidgets.QPushButton(self.tab_symmetric)
        self.decrypt_btn.setObjectName("decrypt_btn")
        self.horizontalLayout_2.addWidget(self.decrypt_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_symmetric_plaintext = QtWidgets.QLabel(self.tab_symmetric)
        self.label_symmetric_plaintext.setObjectName("label_symmetric_plaintext")
        self.horizontalLayout_4.addWidget(self.label_symmetric_plaintext)
        self.symmetric_plaintext = QtWidgets.QPlainTextEdit(self.tab_symmetric)
        self.symmetric_plaintext.setPlainText("")
        self.symmetric_plaintext.setObjectName("symmetric_plaintext")
        self.horizontalLayout_4.addWidget(self.symmetric_plaintext)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_symmetric_ciphertext = QtWidgets.QLabel(self.tab_symmetric)
        self.label_symmetric_ciphertext.setObjectName("label_symmetric_ciphertext")
        self.horizontalLayout_5.addWidget(self.label_symmetric_ciphertext)
        self.symmetric_ciphertext = QtWidgets.QPlainTextEdit(self.tab_symmetric)
        self.symmetric_ciphertext.setPlainText("")
        self.symmetric_ciphertext.setObjectName("symmetric_ciphertext")
        self.horizontalLayout_5.addWidget(self.symmetric_ciphertext)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_symmetric, "")
        self.tab_asymmetric = QtWidgets.QWidget()
        self.tab_asymmetric.setObjectName("tab_asymmetric")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_asymmetric)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_asymmetric_model = QtWidgets.QLabel(self.tab_asymmetric)
        self.label_asymmetric_model.setObjectName("label_asymmetric_model")
        self.horizontalLayout_13.addWidget(self.label_asymmetric_model)
        self.asymmetric_model_combo = QtWidgets.QComboBox(self.tab_asymmetric)
        self.asymmetric_model_combo.setObjectName("asymmetric_model_combo")
        self.asymmetric_model_combo.addItem("")
        self.horizontalLayout_13.addWidget(self.asymmetric_model_combo)
        self.label_asymmetric_key_length = QtWidgets.QLabel(self.tab_asymmetric)
        self.label_asymmetric_key_length.setObjectName("label_asymmetric_key_length")
        self.horizontalLayout_13.addWidget(self.label_asymmetric_key_length)
        self.asymmetric_key_length_combo = QtWidgets.QComboBox(self.tab_asymmetric)
        self.asymmetric_key_length_combo.setObjectName("asymmetric_key_length_combo")
        self.asymmetric_key_length_combo.addItem("")
        self.asymmetric_key_length_combo.addItem("")
        self.asymmetric_key_length_combo.addItem("")
        self.horizontalLayout_13.addWidget(self.asymmetric_key_length_combo)
        self.asymmetric_generate = QtWidgets.QPushButton(self.tab_asymmetric)
        self.asymmetric_generate.setObjectName("asymmetric_generate")
        self.horizontalLayout_13.addWidget(self.asymmetric_generate)
        spacerItem5 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.asymmetric_encrypt = QtWidgets.QPushButton(self.tab_asymmetric)
        self.asymmetric_encrypt.setObjectName("asymmetric_encrypt")
        self.horizontalLayout_13.addWidget(self.asymmetric_encrypt)
        self.asymmetric_decrypt = QtWidgets.QPushButton(self.tab_asymmetric)
        self.asymmetric_decrypt.setObjectName("asymmetric_decrypt")
        self.horizontalLayout_13.addWidget(self.asymmetric_decrypt)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem6)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_public_key = QtWidgets.QLabel(self.tab_asymmetric)
        self.label_public_key.setMinimumSize(QtCore.QSize(0, 18))
        self.label_public_key.setObjectName("label_public_key")
        self.verticalLayout_3.addWidget(self.label_public_key)
        self.public_key = QtWidgets.QPlainTextEdit(self.tab_asymmetric)
        self.public_key.setObjectName("public_key")
        self.verticalLayout_3.addWidget(self.public_key)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_private_key = QtWidgets.QLabel(self.tab_asymmetric)
        self.label_private_key.setMinimumSize(QtCore.QSize(0, 18))
        self.label_private_key.setObjectName("label_private_key")
        self.verticalLayout_4.addWidget(self.label_private_key)
        self.private_key = QtWidgets.QPlainTextEdit(self.tab_asymmetric)
        self.private_key.setObjectName("private_key")
        self.verticalLayout_4.addWidget(self.private_key)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_asymmetric_plaintext = QtWidgets.QLabel(self.tab_asymmetric)
        self.label_asymmetric_plaintext.setMinimumSize(QtCore.QSize(0, 18))
        self.label_asymmetric_plaintext.setObjectName("label_asymmetric_plaintext")
        self.verticalLayout_5.addWidget(self.label_asymmetric_plaintext)
        self.asymmetric_plaintext = QtWidgets.QPlainTextEdit(self.tab_asymmetric)
        self.asymmetric_plaintext.setObjectName("asymmetric_plaintext")
        self.verticalLayout_5.addWidget(self.asymmetric_plaintext)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_asymmetric_ciphertext = QtWidgets.QLabel(self.tab_asymmetric)
        self.label_asymmetric_ciphertext.setMinimumSize(QtCore.QSize(0, 18))
        self.label_asymmetric_ciphertext.setObjectName("label_asymmetric_ciphertext")
        self.verticalLayout_6.addWidget(self.label_asymmetric_ciphertext)
        self.asymmetric_ciphertext = QtWidgets.QPlainTextEdit(self.tab_asymmetric)
        self.asymmetric_ciphertext.setObjectName("asymmetric_ciphertext")
        self.verticalLayout_6.addWidget(self.asymmetric_ciphertext)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.formLayout)
        self.horizontalLayout_9.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_asymmetric, "")
        self.tab_rail = QtWidgets.QWidget()
        self.tab_rail.setObjectName("tab_rail")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_rail)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_fence_num = QtWidgets.QLabel(self.tab_rail)
        self.label_fence_num.setObjectName("label_fence_num")
        self.horizontalLayout_11.addWidget(self.label_fence_num)
        self.rail_fence_num = QtWidgets.QLineEdit(self.tab_rail)
        self.rail_fence_num.setObjectName("rail_fence_num")
        self.horizontalLayout_11.addWidget(self.rail_fence_num)
        self.label_space = QtWidgets.QLabel(self.tab_rail)
        self.label_space.setObjectName("label_space")
        self.horizontalLayout_11.addWidget(self.label_space)
        self.rail_space = QtWidgets.QLineEdit(self.tab_rail)
        self.rail_space.setObjectName("rail_space")
        self.horizontalLayout_11.addWidget(self.rail_space)
        self.rail_encrypt = QtWidgets.QPushButton(self.tab_rail)
        self.rail_encrypt.setObjectName("rail_encrypt")
        self.horizontalLayout_11.addWidget(self.rail_encrypt)
        self.rail_decrypt = QtWidgets.QPushButton(self.tab_rail)
        self.rail_decrypt.setObjectName("rail_decrypt")
        self.horizontalLayout_11.addWidget(self.rail_decrypt)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_rail_plaintext = QtWidgets.QLabel(self.tab_rail)
        self.label_rail_plaintext.setObjectName("label_rail_plaintext")
        self.horizontalLayout_10.addWidget(self.label_rail_plaintext)
        self.rail_plaintext = QtWidgets.QPlainTextEdit(self.tab_rail)
        self.rail_plaintext.setObjectName("rail_plaintext")
        self.horizontalLayout_10.addWidget(self.rail_plaintext)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_rail_ciphertext = QtWidgets.QLabel(self.tab_rail)
        self.label_rail_ciphertext.setObjectName("label_rail_ciphertext")
        self.horizontalLayout.addWidget(self.label_rail_ciphertext)
        self.rail_ciphertext = QtWidgets.QPlainTextEdit(self.tab_rail)
        self.rail_ciphertext.setObjectName("rail_ciphertext")
        self.horizontalLayout.addWidget(self.rail_ciphertext)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tab_rail, "")
        self.tab_parse_headers = QtWidgets.QWidget()
        self.tab_parse_headers.setObjectName("tab_parse_headers")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab_parse_headers)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headers_input = QtWidgets.QPlainTextEdit(self.tab_parse_headers)
        self.headers_input.setObjectName("headers_input")
        self.verticalLayout_2.addWidget(self.headers_input)
        self.headers_output = QtWidgets.QTextBrowser(self.tab_parse_headers)
        self.headers_output.setObjectName("headers_output")
        self.verticalLayout_2.addWidget(self.headers_output)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_parse_headers, "")
        self.tab_msg_queue = QtWidgets.QWidget()
        self.tab_msg_queue.setObjectName("tab_msg_queue")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_msg_queue)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_msg_queue)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_nsq = QtWidgets.QWidget()
        self.tab_nsq.setObjectName("tab_nsq")
        self.groupBox = QtWidgets.QGroupBox(self.tab_nsq)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 221, 171))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.nsq_config_combo = QtWidgets.QComboBox(self.groupBox)
        self.nsq_config_combo.setObjectName("nsq_config_combo")
        self.horizontalLayout_12.addWidget(self.nsq_config_combo)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.nsq_config_text = QtWidgets.QPlainTextEdit(self.groupBox)
        self.nsq_config_text.setObjectName("nsq_config_text")
        self.horizontalLayout_14.addWidget(self.nsq_config_text)
        self.verticalLayout_12.addLayout(self.horizontalLayout_14)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_nsq)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 10, 278, 257))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_15.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_15.addWidget(self.pushButton)
        self.verticalLayout_14.addLayout(self.horizontalLayout_15)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_14.addWidget(self.textBrowser)
        self.verticalLayout_15.addLayout(self.verticalLayout_14)
        self.tabWidget_2.addTab(self.tab_nsq, "")
        self.tab_rabbitmq = QtWidgets.QWidget()
        self.tab_rabbitmq.setObjectName("tab_rabbitmq")
        self.tabWidget_2.addTab(self.tab_rabbitmq, "")
        self.verticalLayout_11.addWidget(self.tabWidget_2)
        self.tabWidget.addTab(self.tab_msg_queue, "")
        self.verticalLayout_8.addWidget(self.tabWidget)

        self.retranslateUi(EncryptForm)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(EncryptForm)

    def retranslateUi(self, EncryptForm):
        _translate = QtCore.QCoreApplication.translate
        EncryptForm.setWindowTitle(_translate("EncryptForm", "工具合集"))
        self.label_mda_mod.setText(_translate("EncryptForm", "模块:"))
        self.mda_mod_combo.setItemText(0, _translate("EncryptForm", "MD5"))
        self.mda_mod_combo.setItemText(1, _translate("EncryptForm", "SHA1"))
        self.mda_mod_combo.setItemText(2, _translate("EncryptForm", "SHA224"))
        self.mda_mod_combo.setItemText(3, _translate("EncryptForm", "SHA256"))
        self.mda_mod_combo.setItemText(4, _translate("EncryptForm", "SHA384"))
        self.mda_mod_combo.setItemText(5, _translate("EncryptForm", "SHA512"))
        self.mda_mod_combo.setItemText(6, _translate("EncryptForm", "HMAC-MD5"))
        self.mda_mod_combo.setItemText(7, _translate("EncryptForm", "HMAC-SHA1"))
        self.mda_mod_combo.setItemText(8, _translate("EncryptForm", "HMAC-SHA224"))
        self.mda_mod_combo.setItemText(9, _translate("EncryptForm", "HMAC-SHA256"))
        self.mda_mod_combo.setItemText(10, _translate("EncryptForm", "HMAC-SHA384"))
        self.mda_mod_combo.setItemText(11, _translate("EncryptForm", "HMAC-SHA512"))
        self.label_mda_salt.setText(_translate("EncryptForm", "盐:"))
        self.label_mda_format.setText(_translate("EncryptForm", "格式:"))
        self.mda_format_combo.setItemText(0, _translate("EncryptForm", "hex"))
        self.mda_format_combo.setItemText(1, _translate("EncryptForm", "base64"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mda), _translate("EncryptForm", "消息摘要"))
        self.label_symmetric_model.setText(_translate("EncryptForm", "模块:"))
        self.symmetric_model_combo.setItemText(0, _translate("EncryptForm", "AES"))
        self.symmetric_model_combo.setItemText(1, _translate("EncryptForm", "DES"))
        self.symmetric_model_combo.setItemText(2, _translate("EncryptForm", "3DES"))
        self.symmetric_model_combo.setItemText(3, _translate("EncryptForm", "RC4"))
        self.label_symmetric_mod.setText(_translate("EncryptForm", "模式:"))
        self.symmetric_mod_combo.setItemText(0, _translate("EncryptForm", "ECB"))
        self.symmetric_mod_combo.setItemText(1, _translate("EncryptForm", "CBC"))
        self.symmetric_mod_combo.setItemText(2, _translate("EncryptForm", "CFB"))
        self.symmetric_mod_combo.setItemText(3, _translate("EncryptForm", "CTR"))
        self.symmetric_mod_combo.setItemText(4, _translate("EncryptForm", "OFB"))
        self.label_symmetric_fill.setText(_translate("EncryptForm", "填充:"))
        self.symmetric_fill_combo.setItemText(0, _translate("EncryptForm", "pkcs7"))
        self.symmetric_fill_combo.setItemText(1, _translate("EncryptForm", "x923"))
        self.symmetric_fill_combo.setItemText(2, _translate("EncryptForm", "iso7816"))
        self.label_symmetric_key_length.setText(_translate("EncryptForm", "密钥长度:"))
        self.symmetric_key_length_combo.setItemText(0, _translate("EncryptForm", "16"))
        self.symmetric_key_length_combo.setItemText(1, _translate("EncryptForm", "24"))
        self.symmetric_key_length_combo.setItemText(2, _translate("EncryptForm", "32"))
        self.label_symmetric_format.setText(_translate("EncryptForm", "格式:"))
        self.symmetric_format_combo.setItemText(0, _translate("EncryptForm", "hex"))
        self.symmetric_format_combo.setItemText(1, _translate("EncryptForm", "base64"))
        self.label_symmetric_key.setText(_translate("EncryptForm", "密钥:"))
        self.label_symmetric_iv.setText(_translate("EncryptForm", "向量:"))
        self.encryption_btn.setText(_translate("EncryptForm", "加密"))
        self.decrypt_btn.setText(_translate("EncryptForm", "解密"))
        self.label_symmetric_plaintext.setText(_translate("EncryptForm", "明文:"))
        self.label_symmetric_ciphertext.setText(_translate("EncryptForm", "密文:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_symmetric), _translate("EncryptForm", "对称加密"))
        self.label_asymmetric_model.setText(_translate("EncryptForm", "模块:"))
        self.asymmetric_model_combo.setItemText(0, _translate("EncryptForm", "RSA"))
        self.label_asymmetric_key_length.setText(_translate("EncryptForm", "密钥长度:"))
        self.asymmetric_key_length_combo.setItemText(0, _translate("EncryptForm", "1024"))
        self.asymmetric_key_length_combo.setItemText(1, _translate("EncryptForm", "2048"))
        self.asymmetric_key_length_combo.setItemText(2, _translate("EncryptForm", "4096"))
        self.asymmetric_generate.setText(_translate("EncryptForm", "生成密钥对"))
        self.asymmetric_encrypt.setText(_translate("EncryptForm", "公钥加密"))
        self.asymmetric_decrypt.setText(_translate("EncryptForm", "私钥解密"))
        self.label_public_key.setText(_translate("EncryptForm", "公钥Public:"))
        self.label_private_key.setText(_translate("EncryptForm", "私钥Private:"))
        self.label_asymmetric_plaintext.setText(_translate("EncryptForm", "明文:"))
        self.label_asymmetric_ciphertext.setText(_translate("EncryptForm", "密文:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_asymmetric), _translate("EncryptForm", "非对称加密"))
        self.label_fence_num.setText(_translate("EncryptForm", "栏数:"))
        self.label_space.setText(_translate("EncryptForm", "分隔符:"))
        self.rail_encrypt.setText(_translate("EncryptForm", "加密"))
        self.rail_decrypt.setText(_translate("EncryptForm", "解密"))
        self.label_rail_plaintext.setText(_translate("EncryptForm", "明文:"))
        self.label_rail_ciphertext.setText(_translate("EncryptForm", "密文:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rail), _translate("EncryptForm", "栅栏加密"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_parse_headers), _translate("EncryptForm", "浏览器请求头格式化"))
        self.groupBox.setTitle(_translate("EncryptForm", "配置"))
        self.groupBox_2.setTitle(_translate("EncryptForm", "状态"))
        self.pushButton.setText(_translate("EncryptForm", "查询"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_nsq), _translate("EncryptForm", "NSQ"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_rabbitmq), _translate("EncryptForm", "Rabbitmq"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_msg_queue), _translate("EncryptForm", "消息队列"))
