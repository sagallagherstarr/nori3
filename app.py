#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 10:42:06 2014

@author: sgallagherstarr
"""
APPNAME = "nori3"

import logging
logging.basicConfig(level=logging.DEBUG,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
nori3log = logging.getLogger(APPNAME)
nori3log.setLevel(logging.DEBUG)
nori3log.debug("App %s launched.", APPNAME)

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
import tornado.web
from tornado.options import define, options
import motor

from restable.resources import models, ModelParams
from restable.handler import rest_routes
from restable.factories import ModelFactory
from restable.register import objects

from addict import Dict
import views

pf = pprint.PrettyPrinter(indent=2).pformat

#motor_client = motor.MotorClient()
#production_db = motor_client.nori3_production # production is the "real" database
#test_db = motor_client.nori3_test # test is for app_testing
#sandbox_db = motor_client.nori3_sandbox # sandbox is for trialing data before committing
# that data to production

settings = Dict()
settings.debug = True
settings.motor_client = motor.MotorClient()
settings.production_db = settings.motor_client.nori3_production
settings.test_db = settings.motor_client.nori3_test
settings.sandbox_db = settings.motor_client.nori3_sandbox

def main():
  port = 8888

  test_resource = ModelFactory(settings.test_db, objects, models, ModelParams)
  production_resource = ModelFactory(settings.production_db, objects, models, ModelParams)
  sandbox_resource = ModelFactory(settings.sandbox_db, objects, models, ModelParams)

  routes = views.routes
  routes = routes + rest_routes(objects, production_resource, route_prefix="/rest")
  routes = routes + rest_routes(objects, test_resource, route_prefix="/test_rest")
  routes = routes + rest_routes(objects, sandbox_resource, route_prefix="/sandbox_rest")
  
  application = Application(routes, **settings)
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(port)
  tornado.ioloop.IOLoop.instance().start()    

if __name__ == "__main__":
  main()
