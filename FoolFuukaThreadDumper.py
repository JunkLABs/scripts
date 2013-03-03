#!/usr/bin/python
'''
FoolFuukaThreadDumper.py
Copyright 2013 Wohlfe
Licensed under the WTFPLv2

Guess what this does? It takes a Foolz archived board and thread and dumps that shit to your hard drive. 
It does it via the API to, like it fucking should. Stop relying on third parties to save your "precious" threads. 
Requires Python 3 and requests. 

Don't abuse the API, it makes Youmu cry. If you use this to try and dump an entire board you are a fucking moron.
https://github.com/FoolCode/FoolFuuka/issues/98#issuecomment-14131740

syntax: FoolFuukaThreadDumper.py <board> <thread>
example: FoolFuukaThreadDumper.py v 12345

Coming soon: 
Make it classy
Maybe some more configuration options
'''

import os
import sys
import requests
import json

if sys.version_info < (3, 0): #Checks the Python version
    raise "You have to use Python 3 or change the script." 

try:
    board_arg = sys.argv[1].rstrip().lower() #Expects a board, strips whitespace from it, makes it lowercase.
    thread_arg = sys.argv[2].rstrip() #Expects a thread, strips whitespace from it.

    if board.startswith('/') or board.endswith('/'): #Checks if someone didn't follow the god damn directions and put slashes in the board name
        board = board.replace('/', '') #Replaces them shits

    if not isinstance(thread, int): #Checks if the thread syntax is an integer
        raise "You fucked up the thread syntax." #If not it tells you how much of an idiot you are
        sys.exit(1)

except IndexError:
    sys.exit("You fucked up the syntax:", err)

def ThreadDump(board, thread):
	payload = {'board': 'board_arg', 'thread': 'thread_arg'}
    request = requests.get('http://archive.foolz.us/_/api/chan/thread', params=payload)