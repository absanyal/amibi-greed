# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:20:39 2017

@author: AB Sanyal
"""

"""
The creature module. It defines the amibi object along with it's genetics. Refer to README.md for details.
"""

#imports
import numpy as np

#Generator for generating unique id number for each amibi
def id_gen():
    i = 1
    while (True):
        yield i
        i += 1

t_idno = id_gen()

#The main creature class
class amibi:

    def __init__( self, t_type = " " ):
        self.idno = next(t_idno)
        self.age = 0
        self.energy = 100

        if ( t_type == " " ): #type is an optional argument. If ommitted, amibi is of random type.
            t_type = np.random.choice( [ "G", "S" ] )

        self.type = t_type