#!/usr/bin/env python
from libmproxy import controller, proxy
from daumdicparser import DaumDicParser
from datetime import datetime
from datamanager import DataManager
import os

class WordSniffer(controller.Master):
    def __init__(self, server):
        controller.Master.__init__(self, server)
        self.daumdicparser = DaumDicParser()
        self.datamanager = DataManager('127.0.0.1', 27017) 

    def run(self):
        print 'proxy server is running on 8080'
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_response(self, msg):
        host = msg.request.host
        path = msg.request.path

        msg.reply()

        if host == 'dic.daum.net' and '/word/view.do' in path:
            word = self.daumdicparser.parse(msg.content)
            word_dict = word.__dict__
            word_dict['inserted_time'] = datetime.now()

            self.datamanager.save(word_dict)
            
config = proxy.ProxyConfig(
    cacert = os.path.expanduser("~/.mitmproxy/mitmproxy-ca.pem")
)
server = proxy.ProxyServer(config, 8080)
m = WordSniffer(server)
m.run()