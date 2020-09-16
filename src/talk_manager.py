from PyQt5.QtCore import QThread

from const import *
from replyer import Replyer
from voiro_acsor import AccessorVoiceroid


class TalkManager(QThread):
    def __init__(self, q, set_guest_name, set_guest_label, set_guest_image, set_voiceroid_label, set_voiceroid_image, set_voiceroid_reply_backcolor):
        super(TalkManager, self).__init__()

        self.q = q
        self.set_guest_name = set_guest_name
        self.set_guest_label = set_guest_label
        self.set_guest_image = set_guest_image
        self.set_voiceroid_label = set_voiceroid_label
        self.set_voiceroid_image = set_voiceroid_image
        self.set_voiceroid_reply_backcolor = set_voiceroid_reply_backcolor

        self.replyer = Replyer()

        # voiceroidエディタ接続
        self.voiro_accessor = AccessorVoiceroid()
        if not self.voiro_accessor.handle:
            print('cannot found voiceroid')
            exit()

    def run(self):
        '''
        チャットから対話要否を判定し、対話取得、各種画面表示、ボイロ制御を行う
        '''

        while True:
            # チャットキューからチャットデータ取得
            chat = self.q.get()
            if not chat:
                continue
            name = chat['name']
            content = chat['content']

            # 対話要否判定
            need, _content, target = self.replyer.need_reply(content)
            if not need:
                continue

            # 対話取得
            reply = self.replyer.get_reply(_content)
            if reply == '':
                reply = CONST_REPLY

            # 各種対話情報画面表示
            self.set_guest_name(name, target)
            self.set_guest_label(_content)
            self.set_voiceroid_label(reply)
            self.set_voiceroid_image(NAME_IMAGE_MAP[target])
            self.set_voiceroid_reply_backcolor(NAME_COLOR_MAP[target])

            # ボイス発声
            self.voiro_accessor.talk(target, reply)
