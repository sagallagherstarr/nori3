# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 11:23:51 2014

@author: scott
"""

import logging
nori3log = logging.getLogger("nori3")
log = nori3log.getChild(__name__)

import json
import bson

from tornado import gen

from schematics.types import StringType, URLType, BooleanType, DateType
from schematics.types.compound import ListType, ModelType
#from mingus.service.models import BaseModel

from Nori3Base import Nori3BaseModel

class SUSHIServiceEndpoint(Nori3BaseModel):
  VendorName = StringType()
  
  Description = StringType(required=False)
  RequestorID = StringType(required=False)
  RequestorName = StringType(required=False)
  RequestorEmail = StringType(required=False)
  CustomerID = StringType(required=False)
  CustomerName = StringType(required=False)
  CounterRelease = StringType(required=False, choices=["1", "2","3", "4"])
#  CounterReportType = StringType(required=False)
  wsdlURL = URLType(required=False)
  ReportsAvailable = ListType(StringType)
  
  VendorRequiresFields = ListType(StringType)
  
@gen.coroutine
def create_test_SUSHIServiceEndpoint(application):
  log.debug("create_test_SUSHIServiceEndpoint entered.")
  db = application.settings["test_db"] # use only the test database
  
#  names = yield db.collection_names()
  
  dr = yield db.drop_collection("sushiserviceendpoint")
  
#  dr2 = yield db.sushiserviceendpoint.drop()
#  
#  d43 = yield db["SUSHIServiceEndpoint".lower()].drop()

#  names = yield db.collection_names()

  EBSCO = SUSHIServiceEndpoint({
    "VendorName": "EBSCOhost",
    "Description": "EBSCOhost SUSHI endpoint",
    "RequestorID": "8746ed38-5d72-44c9-ba06-b0d1d15b3238",
    "RequestorName": "Scott Gallagher-Starr",
    "RequestorEmail": "sgallagherstarr@nwcu.edu",
    "CustomerID": "s8887269",
    "CustomerName": "NCU",
    "CounterRelease": "4",
    "wsdlURL": "http://sushi.ebscohost.com/R4/SushiService.svc",
    "ReportsAvailable": ["JR1", "JR5", "DR1", "DR2", "PR1", "BR1", "BR2", "BR3" ],
    "VendorRequiresFields": ["RequestorID", "CustomerID", "wsdlURL"]
  })
  
  EBSCO.save(db)
  
  log.debug("SUSHIServiceEndpoint created. mro contains: %r", SUSHIServiceEndpoint.__mro__)
    
