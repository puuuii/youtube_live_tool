import requests

from const import *


class Replyer:
    def __init__(self):

        self.data = {
            'apikey': TALK_API_KEY,
            'query': ''
        }

    def need_reply(self, content):
        '''
        対話判断
        '''

        need, _content = self._need_reply(content, TO_YUKARI_LIST)
        if need: return need, _content, YUKARI

        need, _content = self._need_reply(content, TO_MAKI_LIST)
        if need: return need, _content, MAKI

        need, _content = self._need_reply(content, TO_ZUNKO_LIST)
        if need: return need, _content, ZUNKO

        need, _content = self._need_reply(content, TO_AKANE_LIST)
        if need: return need, _content, AKANE

        need, _content = self._need_reply(content, TO_AOI_LIST)
        if need: return need, _content, AOI

        need, _content = self._need_reply(content, TO_KIRITAN_LIST)
        if need: return need, _content, KIRITAN

        return False, None, None

    def _need_reply(self, content, target_list):
        need = False
        _content = content

        checked_list = [content.find(item) for item in target_list]
        for i in range(len(target_list)):
            if checked_list[i] == FOUND_AT_TOP:
                remove_len = len(target_list[i])
                _content = content[remove_len:]
                need = True

        return need, _content

    def get_reply(self, content):
        '''
        対話APIに投げて対話取得
        '''

        self.data['query'] = content

        response = requests.post(TALK_URL, data=self.data)
        reply = ''
        try:
            reply = response.json()['results'][0]['reply']
        except:
            print('api responce error')

        return reply
