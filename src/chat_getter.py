import pywinauto
from PyQt5.QtCore import QThread

from const import *


class ChatGetter(QThread):
    def __init__(self, q):
        super(ChatGetter, self).__init__()

        self.q = q
        self.comment_element = self._get_comment_element()


    def run(self):
        '''
        発言者&コメント取得
        '''

        # 最新チャットを取得し続け、適宜対キューに詰める
        lastchat = {'name': '', 'content': ''}
        while True:
            try:
                tmp_chatinfo = self.comment_element.children()[-1].children()
                name = pywinauto.controls.uia_controls.EditWrapper(tmp_chatinfo[INDEX_USERNAME].children()[0]).texts()[0]
                content = pywinauto.controls.uia_controls.EditWrapper(tmp_chatinfo[INDEX_CONTENT].children()[0]).texts()[0]
            except IndexError:
                pass

            # 前回取得時と同ユーザー&同内容なら無視
            if lastchat['name'] == name and lastchat['content'] == content:
                continue

            # キューに詰める
            self.q.put({'name': name, 'content': content})

            # 最新チャット内容更新
            lastchat['name'] = name
            lastchat['content'] = content

    def _get_comment_element(self):
        '''
        MultiCommentViewからコメント要素取得
        '''

        parentUIAElement = pywinauto.uia_element_info.UIAElementInfo()
        handle = self._search_child(WINDOWNAME_COMMENT_VIEWER, parentUIAElement)
        if not handle:
            print('not found MultiCommentView')
            exit()

        comment_element = self._search_child(CLASSNAME_COMMENTDATAGRID, handle)
        comment_element = self._search_child(CLASSNAME_DATAGRID, comment_element)

        return comment_element


    def _search_child(self, name, uiaElementInfo):
        '''
        ハンドル検索&取得
        '''

        for childElement in uiaElementInfo.iter_children():
            if (name in childElement.name) or (name in childElement.class_name):
                return childElement

        return None
