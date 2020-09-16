import pywinauto
from PyQt5.QtCore import QThread

from const import *


class AccessorVoiceroid:
    def __init__(self, windowname='VOICEROID2'):
        parentUIAElement = pywinauto.uia_element_info.UIAElementInfo()
        self.handle = self._search_child_byname(windowname, parentUIAElement)


    def _search_child_byname(self, name, uiaElementInfo):
        '''
        ハンドル検索&取得
        '''
        # 全ての子要素を検索し、なければNoneを返す
        searched_tuple = (name, f"{name}*")
        for childElement in uiaElementInfo.iter_children():
            if childElement.name in searched_tuple:
                return childElement

        return None

    def talk(self, target, phrase):
        '''
        会話実行
        '''

        _phrase = f"{NAME_PREFIX_MAP[target]}{phrase}"

        try:
            # テキスト要素のElementInfoを取得
            TextEditViewEle = self._search_child_byclassname("TextEditView", self.handle)
            textBoxEle      = self._search_child_byclassname("TextBox", TextEditViewEle)

            # コントロール取得
            textBoxEditControl = pywinauto.controls.uia_controls.EditWrapper(textBoxEle)

            # テキスト登録
            textBoxEditControl.set_edit_text(_phrase)

            # ボタン取得
            buttonsEle = self._search_child_byclassname("Button", TextEditViewEle, target_all=True)
            # 再生ボタンを探す
            playButtonEle = ""
            for buttonEle in buttonsEle:
                # テキストブロックを捜索
                textBlockEle = self._search_child_byclassname("TextBlock", buttonEle)
                if textBlockEle.name == "再生":
                    playButtonEle = buttonEle
                    break

            # ボタンコントロール取得
            playButtonControl = pywinauto.controls.uia_controls.ButtonWrapper(playButtonEle)

            # 再生ボタン押下
            playButtonControl.click()
        except:
            print('error')
            pass

    def _search_child_byclassname(self, class_name, uiaElementInfo, target_all=False):
        target = []
        # 全ての子要素検索
        for childElement in uiaElementInfo.children():
            # ClassNameの一致確認
            if childElement.class_name == class_name:
                if target_all == False:
                    return childElement
                else:
                    target.append(childElement)
        if target_all == False:
            # 無かったらFalse
            return False
        else:
            return target
