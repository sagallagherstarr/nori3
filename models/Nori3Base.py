# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 19:23:09 2014

@author: scott
"""

import logging
nori3log = logging.getLogger("nori3")
log = nori3log.getChild(__name__)

import json
#import bson

import arrow

from tornado import gen

from schematics.types import StringType, URLType, BooleanType, DateTimeType, IntType
#from schematics.types.compound import ListType, ModelType
#from mingus.service.models import BaseModel
#from motorm import AsyncModel

from restable.AsyncModel import AsyncModel

class AbstractModelError(NotImplementedError):
  pass

def current_time():
  return arrow.now().datetime

class Nori3BaseModel(AsyncModel):
  is_active = BooleanType(required=True, default=True)
  
  creation_date = DateTimeType(required=False, default=None)
  last_update = DateTimeType(required=True, default=current_time)
  
  def activate(self):
    self.is_active = True
  
  def deactivate(self):
    self.is_active = False
  
  def to_primitive(self):
    """By default, mingus models include a null _id field. This interferes
       with our ability to save new models, so pop out a null _id field. If
       _id is not null, leave it alone.
    """
    retval = super(Nori3BaseModel, self).to_primitive()
    
    if retval["_id"] is None:
      retval.pop("_id")
    
    return retval
  
  def save(self, db, **kwargs):
    if hasattr(self, "_id") and self._id is None:
      delattr(self, "_id")
    
    super(Nori3BaseModel, self).save(db, **kwargs)