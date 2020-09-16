import os


WINDOWNAME_COMMENT_VIEWER = 'MultiCommentViewer'
CLASSNAME_COMMENTDATAGRID = 'CommentDataGrid'
CLASSNAME_DATAGRID = 'DataGrid'
INDEX_USERNAME = 3
INDEX_CONTENT = 4

TALK_URL = 'https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk'
TALK_API_KEY = os.environ['TALK_API_KEY']

CREDENTIAL_PATH = 'credentials.json'
CLIENT_JSON_PATH = 'client.json'
CREDENTIAL_PATH2 = 'credentials2.json'
CLIENT_JSON_PATH2 = 'client2.json'

GOOGLE_API_SCOPE = 'https://www.googleapis.com/auth/youtube.readonly'
BROADCAST_URL = 'https://www.googleapis.com/youtube/v3/liveBroadcasts?part=snippet&maxResults=1&mine=true&fields=items(snippet(liveChatId))'
MESSAGES_URL = 'https://www.googleapis.com/youtube/v3/liveChat/messages?part=snippet,authorDetails&fields=items(snippet(textMessageDetails(messageText)),authorDetails(displayName,profileImageUrl)),nextPageToken'

UI_PATH = 'ui/untitled.ui'

QUOTA_EXCEEDED = 'quotaExceeded'
DAILY_LIMIT_EXCEEDED = 'dailyLimitExceeded'

YUKARI = '結月ゆかり'
MAKI = '弦巻マキ'
ZUNKO = '東北ずん子'
AKANE = '琴葉茜'
AOI = '琴葉葵'
KIRITAN = '東北きりたん'

NAME_IMAGE_MAP = {
    YUKARI: 'resource/image/yukari.png',
    MAKI: 'resource/image/maki.png',
    ZUNKO: 'resource/image/zunko.png',
    AKANE: 'resource/image/akane.png',
    AOI: 'resource/image/aoi.png',
    KIRITAN: 'resource/image/kiritan.png',
}

NAME_COLOR_MAP = {
    YUKARI: '(238, 213, 244)',
    MAKI: '(254, 243, 180)',
    ZUNKO: '(153, 179, 147)',
    AKANE: '(253, 206, 226)',
    AOI: '(211, 227, 255)',
    KIRITAN: '(188, 158, 179)',
}

NAME_PREFIX_MAP = {
    YUKARI: '結月ゆかり＞',
    MAKI: '民安ともえ(v1)＞',
    ZUNKO: '東北ずん子(v1)＞',
    AKANE: '琴葉 茜(v1)＞',
    AOI: '琴葉 葵(v1)＞',
    KIRITAN: '東北きりたん(v1)＞',
}

FOUND_AT_TOP = 0

TO_YUKARI_LIST = [
    '結月ゆかり>',
    '結月ゆかり＞',
    'ゆかり>',
    'ゆかり＞',
    'ゆかりん>',
    'ゆかりん＞',
    'ゆかりさん>',
    'ゆかりさん＞',
    'ゆかちゃん>',
    'ゆかちゃん＞',
    'ゆかりちゃん>',
    'ゆかりちゃん＞',
    '結月ゆかり)',
    '結月ゆかり）',
    'ゆかり)',
    'ゆかり）',
    'ゆかりん)',
    'ゆかりん）',
    'ゆかりさん)',
    'ゆかりさん）',
    'ゆかちゃん)',
    'ゆかちゃん）',
    'ゆかりちゃん)',
    'ゆかりちゃん）',
]
TO_MAKI_LIST = [
    '弦巻マキ>',
    '弦巻マキ＞',
    'マキ>',
    'マキ＞',
    'まき>',
    'まき＞',
    'マキさん>',
    'マキさん＞',
    'まきさん>',
    'まきさん＞',
    'マキちゃん>',
    'マキちゃん＞',
    'まきちゃん>',
    'まきちゃん＞',
    'マキマキ>',
    'マキマキ＞',
    'まきまき>',
    'まきまき＞',
    '弦巻マキ)',
    '弦巻マキ）',
    'マキ)',
    'マキ）',
    'まき)',
    'まき）',
    'マキさん)',
    'マキさん）',
    'まきさん)',
    'まきさん）',
    'マキちゃん)',
    'マキちゃん）',
    'まきちゃん)',
    'まきちゃん）',
    'マキマキ)',
    'マキマキ）',
    'まきまき)',
    'まきまき）',
]
TO_ZUNKO_LIST = [
    '東北ずん子>',
    '東北ずん子＞',
    'ずんこ>',
    'ずんこ＞',
    'ずん子>',
    'ずん子＞',
    'ずんこさん>',
    'ずんこさん＞',
    'ずん子さん>',
    'ずん子さん＞',
    'ずんちゃん>',
    'ずんちゃん＞',
    '東北ずん子)',
    '東北ずん子）',
    'ずんこ)',
    'ずんこ）',
    'ずん子)',
    'ずん子）',
    'ずんこさん)',
    'ずんこさん）',
    'ずん子さん)',
    'ずん子さん）',
    'ずんちゃん)',
    'ずんちゃん）',
]
TO_AKANE_LIST = [
    '琴葉茜>',
    '琴葉茜＞',
    'あかね>',
    'あかね＞',
    'あかねちゃん>',
    'あかねちゃん＞',
    '茜>',
    '茜＞',
    '茜ちゃん>',
    '茜ちゃん＞',
    '琴葉茜)',
    '琴葉茜）',
    'あかね)',
    'あかね）',
    'あかねちゃん)',
    'あかねちゃん）',
    '茜)',
    '茜）',
    '茜ちゃん)',
    '茜ちゃん）',
]
TO_AOI_LIST = [
    '琴葉葵>',
    '琴葉葵＞',
    'あおい>',
    'あおい＞',
    'あおいちゃん>',
    'あおいちゃん＞',
    '葵>',
    '葵＞',
    '葵ちゃん>',
    '葵ちゃん＞',
    '琴葉葵)',
    '琴葉葵）',
    'あおい)',
    'あおい）',
    'あおいちゃん)',
    'あおいちゃん）',
    '葵)',
    '葵）',
    '葵ちゃん)',
    '葵ちゃん）',
]
TO_KIRITAN_LIST = [
    '東北きりたん>',
    '東北きりたん＞',
    'きりたん>',
    'きりたん＞',
    '東北きりたん)',
    '東北きりたん）',
    'きりたん)',
    'きりたん）',
]

CONST_REPLY = '誤字脱字はありませんか？\nもう一度話しかけてください'