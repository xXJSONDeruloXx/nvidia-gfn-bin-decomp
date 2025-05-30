# Source Generated with Decompyle++
# File: translate.pyc (Python 3.10)

import os
import sys
import json
import locale
import logging
NV_DEFAULT_LOCALE = 'en_US'

class Translate:
    
    def __init__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_lang(self):
        return self.locale

    
    def text(self, category, sub_category, key, keys_to_be_replaced = ([],)):
        msg = self.locale_dict.get(category, { }).get(sub_category, { }).get(key, '')
        if isinstance(msg, list):
            msg = '\n'.join((lambda .0: [ '∙  ' + line for line in .0 ])(msg))
        if keys_to_be_replaced:
            for key in keys_to_be_replaced:
                msg = msg.replace('{{' + key + '}}', keys_to_be_replaced.get(key, ''))
        if '{{' in msg or '}}' in msg:
            logging.error(f'''Key expansion failed: {msg}''')
        return msg


if __name__ == '__main__':
    print(Translate().text('install', 'success', 'title', {
        'APP_NAME': 'GeForce NOW' }))
    return None
