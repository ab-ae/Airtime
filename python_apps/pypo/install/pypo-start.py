#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

if os.geteuid() != 0:
    print "Please run this as root."
    sys.exit(1)
    
try:
    print "Starting daemontool script pypo"
    os.system("svc -u /etc/service/pypo")
        
    print "Starting daemontool script pypo-liquidsoap"
    os.system("svc -u /etc/service/pypo-liquidsoap")
    
except Exception, e:
    print "exception:" + str(e)