import queue
import sys

import requests
from PyQt5 import QtGui, QtWidgets, uic

from chat_getter import ChatGetter
from const import *
from talk_manager import TalkManager


class TubeTool(QtWidgets.QMainWindow):
    def __init__(self):

        q = queue.Queue()

        # 対話管理クラス作成
        self.talkmanager = TalkManager(
            q,
            self.set_guest_name,
            self.set_guest_label,
            self.set_guest_image,
            self.set_voiceroid_label,
            self.set_voiceroid_image,
            self.set_voiceroid_reply_backcolor
        )
        self.talkmanager.start()

        # コメントを取得しキューに詰めるインスタンス作成
        self.chatgetter = ChatGetter(q)
        self.chatgetter.start()

        # UI起動
        super(TubeTool, self).__init__()
        uic.loadUi(UI_PATH, self)
        self.show()

    def set_guest_name(self, name, target):
        self.lbl_guest_name.setText(f"{name} > {target}")

    def set_guest_label(self, comment):
        self.lbl_guest_comment.setText(comment)

    def set_guest_image(self, url):
        data = requests.get(url, stream=True).content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(data)
        self.pixmap_guest.setPixmap(pixmap)

    def set_voiceroid_label(self, comment):
        self.lbl_voiceroid_reply.setText(comment)

    def set_voiceroid_image(self, path):
        self.pixmap_voiceroid.setPixmap(QtGui.QPixmap(path))

    def set_voiceroid_reply_backcolor(self, color):
        self.lbl_voiceroid_reply.setStyleSheet(
            f"background-color:rgb{color};\n"
            "border-style: outset;\n"
            "border-width: 1px;\n"
            "border-radius: 14px;\n"
            "border-color: white;\n"
            "padding: 4px;\n"
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TubeTool()
    app.exec_()
