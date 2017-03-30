#!/usr/bin/env python
# encoding:utf-8
from __future__ import print_function
import os
import logging
import time
import datetime
from  pyinotify import  WatchManager, Notifier,ProcessEvent,IN_DELETE, IN_CREATE,IN_MODIFY

class process_logg:
    logging.basicConfig(level=logging.INFO,filename='/var/log/monitor.log')
    logging.info("Starting monitor...")
    def process_logging(self,event):
        print  ("{1} file: {0} ".format(os.path.join(event.path,event.name),event.maskname.split('_')[1]))
        logging.info("ACCESS event : %s  %s" % (os.path.join(event.path,event.name),datetime.datetime.now()))


class EventHandler(ProcessEvent,process_logg):
    def process_IN_CREATE(self, event):
        self.process_logging(event)

    def process_IN_DELETE(self, event):
        self.process_logging(event)

    def process_IN_MODIFY(self, event):
        self.process_logging(event)


class FileSystemMonitor(EventHandler):
        def __init__(self,path,mask):
            self.path=path
            self
        def run(self):
            wm= WatchManager()
            mask= IN_DELETE | IN_CREATE |IN_MODIFY
            notifier= Notifier(wm, EventHandler())
            wm.add_watch(self.path, mask,rec=True)
            print('now starting monitor {0}'.format(self.path))
            while True:
                try:
                       notifier.process_events()
                       if notifier.check_events():
                               notifier.read_events()
                except KeyboardInterrupt:
                       notifier.stop()
                       break
if __name__ =="__main__":
    monitor = FileSystemMonitor('/tmp')
    monitor.run()
