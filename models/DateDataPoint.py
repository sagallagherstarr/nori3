# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 13:45:19 2014

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
from Nori3Base import Nori3BaseModel

class DateDataPoint(Nori3BaseModel):
  month = StringType()
  year = StringType()
  
  count = IntType()
