import json
from PyQt5.QtWidgets import QMessageBox


class MsgQueueForm:

    def __init__(self):
        self.nsq_config_combo.currentTextChanged.connect(self.change_nsq_config)
        with open("config/cfg/nsq_config.json", encoding="utf-8") as f:
            self.nsq_cfg_json = json.load(f)

        cfg_keys = list(self.nsq_cfg_json.keys())
        self.nsq_config_combo.addItems(cfg_keys)

    def save_nsq_cfg(self):
        try:
            k = self.nsq_config_combo.currentText()
            v = json.loads(self.nsq_config_text.toPlainText())
            self.nsq_cfg_json[k] = v
            with open("config/cfg/nsq_config.json", "w", encoding="utf-8") as f:
                json.dump(self.nsq_cfg_json, f, ensure_ascii=False, indent=4)
        except Exception as e:
            QMessageBox.about(self, "错误", str(e))

    def change_nsq_config(self):
        self.nsq_config_text.setPlainText(json.dumps(self.nsq_cfg_json[self.nsq_config_combo.currentText()], ensure_ascii=False, indent=4))
