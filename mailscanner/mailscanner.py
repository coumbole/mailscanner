#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import imaplib
import configparser
import os
import email
import email.parser
from email.header import decode_header
from pprint import pprint

CONFIG_PATH = os.path.abspath('../.env/conf.ini')
print('Config path: ' + CONFIG_PATH)

def open_connection(verbose=False):

    # Read config file
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    # Connect to server
    hostname = config.get('IMAP', 'hostname')
    if verbose:
        print('Connecting to ' + hostname)
    connection = imaplib.IMAP4_SSL(hostname)

    # Authenticate
    username = config.get('IMAP', 'username')
    password = config.get('IMAP', 'password')
    if verbose:
        print('Logging in as', username)
    connection.login(username, password)

    return connection


# Param: email.message.Message object
# Returns: string containing the message body
def decode_message_body(msg):
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            cdispo = str(part.get('Content-Disposition'))

            # skip any text/plain (txt) attachments
            if ctype == 'text/plain' and 'attachment' not in cdispo:
                body = part.get_payload(decode=True)  # decode
                break

    # not multipart - i.e. plain text, no attachments, keeping fingers crossed
    else:
        body = msg.get_payload(decode=True)
    return body.decode('UTF-8')


"""
    Params:
        conn        IMAP4_SSL connection
        directory   The IMAP directory to look for
        readonly    readonly mode, true or false
"""
def fetch_all_messages(conn, directory, readonly):
    conn.select(directory, readonly)

    typ, data = conn.search(None, 'All')
    for num in data[0].split():
        typ, data = conn.fetch(num, '(RFC822)')
        parse_imap_response(data)

#for header in ['subject', 'to', 'from']:
#    text, encoding = decode_header(msg[header])[0]
#    print('{:^8}: {}'.format(
#        header.upper(), text))



def parse_imap_response(data):
    bodies = {}
    for response_part in data:
        if isinstance(response_part, tuple):
            email_parser = email.parser.BytesFeedParser()
            email_parser.feed(response_part[1])
            msg = email_parser.close()
            body = decode_message_body(msg)
            bodies
            print(body)


#imaplib.Debug = 4
if __name__ == '__main__':
    with open_connection(verbose=True) as c:
        fetch_all_messages(c, 'Recruitment', True)
