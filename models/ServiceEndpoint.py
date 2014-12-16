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
from mingus.service.models import BaseModel

class SUSHIServiceEndpoint(BaseModel):
  class Options:
    namespace = "SUSHIServiceEndpoint"
  
  VendorName = StringType()
  
  Description = StringType(required=False)
  RequestorID = StringType(required=False)
  RequestorName = StringType(required=False)
  RequestorEmail = StringType(required=False)
  CustomerID = StringType(required=False)
  CustomerName = StringType(required=False)
  CounterRelease = StringType(required=False)
#  CounterReportType = StringType(required=False)
  wsdlURL = URLType(required=False)
  ReportsAvailable = ListType(StringType)
  
  VendorRequiresFields = ListType(StringType)
  
  def to_primitive(self):
    """By default, mingus models include a null _id field. This interferes
       with our ability to save new models, so pop out a null _id field. If
       _id is not null, leave it alone.
    """
    retval = super(SUSHIServiceEndpoint, self).to_primitive()
    
    if retval["_id"] is None:
      retval.pop("_id")
    
    return retval
  
  @gen.coroutine
  def save(self, db):
    log.debug("SUSHIServiceEndpoint.save")
    log.debug("  db is %s", db)
    
    log.debug("  self.to_primitive returns %r", json.dumps(self.to_primitive()))
    yield db[self._options.namespace].save(self.to_primitive())
  
@gen.coroutine
def create_test_SUSHIServiceEndpoint(application):
  log.debug("create_test_SUSHIServiceEndpoint entered.")
  db = application.settings["test_db"] # use only the test database
  db.drop_collection("SUSHIServiceEndpoint")
  
#  document = yield db["SUSHIServiceEndpoint"].find_one({"VendorName": "EBSCOhost"})
#  log.debug("  document is %r", document)
#  
#  eb = []
  
#  eb = yield SUSHIServiceEndpoint.objects.filter(VendorName="EBSCOhost", database_name="TEST").find_all()
  
#  if len(eb) == 0:
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
  
  EBSCO.validate()
  
  EBSCO.save(db)
    
