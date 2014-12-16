#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 10:42:06 2014

@author: sgallagherstarr
"""

import os
import os.path
import sys

appbasedir = os.getcwd()
mylibdir = os.path.join(appbasedir, "lib")
mymodelsdir = os.path.join(appbasedir, "models")
myviewsdir = os.path.join(appbasedir, "views")

sys.path = [ appbasedir, mylibdir, mymodelsdir, myviewsdir, ] + sys.path

import pprint
import tornado
from tornado.web import Application
import tornado.httpserver
import tornado.ioloop
#import tornado.options
#import tornado.web
#import tornado.httpserver
#import tornado.ioloop
#import tornado.options
import tornado.web
from tornado.options import define, options
import motor

from mingus.resources import models, ModelParams
from mingus.handler import rest_routes
from mingus.factories import ModelFactory
from mingus.register import objects

APPNAME = "nori3"

import logging
logging.basicConfig(level=logging.DEBUG,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
nori3log = logging.getLogger(APPNAME)
nori3log.setLevel(logging.DEBUG)
nori3log.debug("App %s launched.", APPNAME)

pf = pprint.PrettyPrinter(indent=2).pformat


import views

db = motor.MotorClient().nori3_database
settings = {
  "debug": True,
  "db": db,
}

def main():
  port = 8888

  resource = ModelFactory(db, objects, models, ModelParams)

  routes = rest_routes(objects, resource, route_prefix="/rest") + views.routes
  application = Application(routes, debug=True)
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(port)
  tornado.ioloop.IOLoop.instance().start()    

if __name__ == "__main__":
  main()
