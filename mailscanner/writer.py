#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import imaplib
import time
import email.message

class EmailWriter:

    # TODO: Import settings from config file
    def __init__(self):
        self.new_message = email.message.Message()

    # TODO: Modify to only create the message
    def create_new_msg(self, conn, payload):
        self.new_message.set_unixfrom('Athene rekrybot')
        self.new_message['Subject'] = 'Recruitment mail'
        self.new_message['From'] = 'yrityssuhteet@athene.fi'
        self.new_message['To'] = 'ville.kumpulainen@aalto.fi'
        self.new_message.set_payload(payload)

        conn.append('Drafts', '',
                imaplib.Time2Internaldate(time.time()),
                str(self.new_message).encode('utf-8'))
        #conn.select('Drafts')

    # TODO: Add new method for actually uploading the message
