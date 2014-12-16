# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 11:59:39 2014

@author: scott
"""

from tornado import gen
from tornado.web import RequestHandler

from models import create_test_SUSHIServiceEndpoint

class PopulateTestDataHandler(RequestHandler):
  @gen.coroutine
  def get(self):
    yield create_test_SUSHIServiceEndpoint(self.application)
    
    self.write("Done.")
    
routes = [ (r"/populate_test_data", PopulateTestDataHandler) ]
    