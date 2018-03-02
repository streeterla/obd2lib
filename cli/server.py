# -*- coding: utf-8 -*-

import json
import logging
import threading
import Queue

import WSGIServer

from flask import Flask
from flask import render_template
from flask import Response
from flask import request

from obd2lib.elmdb import ELMdb
from obd2lib.elmdecoder import decode_answer


SUPPORTED_PIDS = None
QUEUE = Queue.Queue()

app = Flask(__name__)
app.debug = True




class ServerMode(threading.Thread):

    def __init__(self, supported_pids):
        global SUPPORTED_PIDS
        SUPPORTED_PIDS = supported_pids

        super(ServerMode, self).__init__()

    def run(self):
        logging.info('Launching server on 127.0.0.1:5000')
        http_server = WSGIServer(('127.0.0.1', 5000), app)
        http_server.serve_forever()
