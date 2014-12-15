# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 10:42:06 2014

@author: sgallagherstarr
"""

import os
import os.path
import sys
import pprint

import logging
logging.basicConfig(level=logging.DEBUG,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
nori2log = logging.getLogger("nori2")
nori2log.setLevel(logging.DEBUG)
nori2log.debug("App launched.")


pf = pprint.PrettyPrinter(indent=2).pformat

appbasedir = os.environ.get("OPENSHIFT_REPO_DIR", ".")
mylibdir = os.path.join(appbasedir, "lib")
mymodelsdir = os.path.join(appbasedir, "models")
myviewsdir = os.path.join(appbasedir, "views")

sys.path = [ appbasedir, mylibdir, mymodelsdir, myviewsdir, ] + sys.path

import tornado
#from tornado import gen
from tornado.web import Application
#from tornado.httpserver import HTTPServer

#import tornado
#from tornado import ioloop
#from tornado import web

import motor

db = motor.MotorClient().test_database

#application = tornado.web.Application([
application = Application([
    (r'/', MainHandler)
], db=db)

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()
