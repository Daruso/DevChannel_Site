import json
import time

import requests

from apps import invite_config, database

lang_channels = {
    'python': invite_config.CH_PYTHON,
    'python2': invite_config.CH_PYTHON,
    'python3': invite_config.CH_PYTHON,

    'cpp': invite_config.CH_CPP,
    'c++': invite_config.CH_CPP,

    'csharp': invite_config.CH_C_SHARP,
    'c#': invite_config.CH_C_SHARP,

    'haskell': invite_config.CH_HASKELL,

    'go': invite_config.CH_GO,

    'ruby': invite_config.CH_RUBY,
    'ror': invite_config.CH_RUBY,

    'swift': invite_config.CH_SWIFT,

    'html': invite_config.CH_WEB,
    'css': invite_config.CH_WEB,
    'javascript': invite_config.CH_WEB,
    'js': invite_config.CH_WEB,
    'jquery': invite_config.CH_WEB,

    'java': invite_config.CH_JAVA,

    'unity': invite_config.CH_GAMEDEV,
    'unityscript': invite_config.CH_GAMEDEV,
    'unity3d': invite_config.CH_GAMEDEV,
    'ue': invite_config.CH_GAMEDEV,
    'ue3': invite_config.CH_GAMEDEV,
    'unrealengine': invite_config.CH_GAMEDEV
}


def send_invite(email, skills):
    # remove all whitespace hack, then lowercase and split by ,
    languages = ''.join(skills.split()).lower().split(',')

    join_these = ','.join(lang_channels[lang] for lang in languages if lang in lang_channels)

    response = requests.post(invite_config.SLACK_INV_URL,
                             params={
                                 'token': invite_config.TOKEN,
                                 'channels': join_these + invite_config.AUTO_JOIN_CHANNELS,
                                 't': round(time.time()),
                                 'email': email,
                                 'first_name': '',
                                 'set_active': 'true',
                                 '_attempts': '1'}
                             )
    dict_data = json.loads(response.text)
    if not dict_data['ok']:
        err = dict_data['error']
        if err == 'invalid_email':
            return -1, 'Sorry, invalid email :('

        elif err == 'already_in_team':
            return 1, 'Sorry, it looks like you are already signed up<br>' \
                      'You will be redirected to devchannel.slack.com'

        elif err == 'already_invited':
            return -1, "It looks like you have already been invited, please look in your mail box (and your spam box " \
                       "too) for an invite.<br>" \
                       "If you can't find it, please contact me on:<br>" \
                       "Reddit: therightman_<br>" \
                       "Twitter: @therightmandev"
        else:
            return -1, dict_data['error']

    elif dict_data['ok']:
        database.insert_user(skills=skills, email=email)
        return 0, 'Check your mail box :)'
