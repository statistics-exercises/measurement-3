import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_exists(self) : 
        self.assertTrue( "xbar" in globals(), "The variable xbar is not defined" )
        
   def test_values(self) : 
       mmm = sum(radii)/len(radii)
       self.assertTrue( xbar==mmm, "xbar has not been calculated correctly" )
