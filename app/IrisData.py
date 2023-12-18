# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class IrisNewData(BaseModel):
    """
    Class to receive the parameters from the api post
    """
    sepal_length: float 
    sepal_width: float 
    petal_length: float 
    petal_width: float