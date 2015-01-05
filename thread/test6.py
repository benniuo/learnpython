#!/usr/bin/env python

# -*- coding: utf-8 -*- 
'''
Created on 2012-8-8

@author: jeromewei
 '''   
from threading import Thread
import time
class race(Thread):
    def __init__(self,threadname,interval):
        Thread.__init__(self,name=threadname)
        self.interval = interval
        self.isrunning = True
    def run(self):
        while self.isrunning:
            print 'thread %s is running,time:%s\n' %(self.getName(),time.ctime())
            time.sleep(self.interval)
    def stop(self):
        self.isrunning = False

def test():
    thread1 = race('A',1)
    thread2 = race('B',1)
    thread1.start()
    thread2.start()
    time.sleep(5)
    thread1.stop()
    thread2.stop()
    
if __name__ =='__main__':
    test()