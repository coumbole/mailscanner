#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import imaplib
import configparser
import os

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


    username = config.get('IMAP', 'username')
    password = config.get('IMAP', 'password')
    if verbose:
        print('Logging in as', username)
    connection.login(username, password)

    return connection


if __name__ == '__main__':
    with open_connection(verbose=True) as c:
        print(c)
