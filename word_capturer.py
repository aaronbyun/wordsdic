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
        self.datamanager = DataManager('192.168.219.151', 27017)

    def run(self):
        print 'proxy server is running on 8080'
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_response(self, msg):
        host = msg.request.host
        path = msg.request.path

        if host == 'dic.daum.net' and '/word/view.do' in path:
            word = self.daumdicparser.parse(msg.content)
            word_dict = word.__dict__
            word_dict['inserted_time'] = datetime.now()

            self.datamanager.save(word_dict)
            
            #'/search.do?dic=eng&q=dissemble'
            #'/word/view.do?wordid=ekw000048341&q=dissemble'
        msg.reply()

config = proxy.ProxyConfig(
    cacert = os.path.expanduser("~/.mitmproxy/mitmproxy-ca.pem")
)
server = proxy.ProxyServer(config, 8080)
m = WordSniffer(server)
m.run()