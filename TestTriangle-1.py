# -*- coding: utf-8 -*-
"""
The primary goal of this file To wirte unit Test for Triangle.py and comply with homework

@author: Rongda Kang

"""

import unittest
import datetime

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalidInput_01(self):
        #Testing lower limit of value 
        self.assertEqual(classifyTriangle(1,0,3),'InvalidInput','1,0,3 is not a triangle')
        
    def testInvalidInput_02(self):
        self.assertEqual(classifyTriangle(1,3,0),'InvalidInput','1,3,0 is not a triangle')
        
    def testInvalidInput_03(self):
        self.assertEqual(classifyTriangle(0,1,3),'InvalidInput','0,1,3 is not a triangle')

    def testInvalidInput_04(self):        
        #Testing Upper Limit of value      
        self.assertEqual(classifyTriangle(201,1,3),'InvalidInput','0,1,3 is not a triangle')
        
    def testInvalidInput_05(self):       
        self.assertEqual(classifyTriangle(1,201,3),'InvalidInput','0,1,3 is not a triangle')
        
    def testInvalidInput_06(self):        
        self.assertEqual(classifyTriangle(1,3,201),'InvalidInput','0,1,3 is not a triangle')
        
    def testInvalidInput_07(self):        
        #Testing Invalid Type input       
        self.assertEqual(classifyTriangle('a',1,1),'InvalidInput','a,1,1 is not a triangle')
    def testInvalidInput_08(self):
        self.assertEqual(classifyTriangle(1,'a',1),'InvalidInput','1,a,1 is not a triangle')
    def testInvalidInput_09(self):
        self.assertEqual(classifyTriangle(1,1,'a'),'InvalidInput','1,1,a is not a triangle')

    def testNotaTriangle_01(self):
        #Testing Invalid Triangle
        self.assertEqual(classifyTriangle(1,1,3),'NotATriangle','1,1,3 is NotATriangle')
    def testNotaTriangle_02(self):
        self.assertEqual(classifyTriangle(3,1,1),'NotATriangle','3,1,1 is NotATriangle')
    def testNotaTriangle_03(self):
        self.assertEqual(classifyTriangle(1,3,1),'NotATriangle','1,3,1 is NotATriangle')
        #Testing Invalid Triangle

    def testRightTriangle_01(self):
        #Testing Upper Limit of value
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangle_02(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def testRightTriangle_03(self):
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,5,4 is a Right triangle')

    def testIsocelesTriangle_01(self):
        #Testing IsocelesTriangle
        self.assertEqual(classifyTriangle(2,3,3),'Isoceles','2,3,3 should be isoceles')
    def testIsocelesTriangle_02(self):
        self.assertEqual(classifyTriangle(3,2,3),'Isoceles','3,2,3 should be isoceles')
    def testIsocelesTriangle_03(self):
        self.assertEqual(classifyTriangle(3,3,2),'Isoceles','3,3,2 should be isoceles')
    
        
    def testScaleneTriangles_01(self):
        #Testing ScaleneTriangles
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be scalene')
    def testScaleneTriangles_02(self):
        self.assertEqual(classifyTriangle(2,4,3),'Scalene','2,4,3 should be scalene')
    def testScaleneTriangles_03(self):
        self.assertEqual(classifyTriangle(4,3,2),'Scalene','4,3,3 should be scalene')
                         
    def testEquilateralTriangles_01(self):
        #Testing EquilateralTriangles
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testEquilateralTriangles_02(self):
        self.assertEqual(classifyTriangle(100,100,100),'Equilateral','100,100,100 should be equilateral')

def my_brand(assignment_name):
    print("=*=*=*= Rongda Kang =*=*=*=")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*=")
    print("=*=*=*= Assignment Name: {} =*=*=*=".format(assignment_name))
    print("=*=*=*= {} function was called =*=*=*=".format(datetime.datetime.now()))

if __name__ == '__main__':
    my_brand('HW-02a Testing Lagacy Porgram')
    print('\n')
    print('Running unit tests')
    unittest.main()
    print('\n')
    my_brand('HW-02a Testing Lagacy Porgram')

