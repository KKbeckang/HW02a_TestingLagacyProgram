*# -\*- coding: utf-8 -\*-*

*"""*

*Assignment Description: Assignment for Rongda Kang this a edited version of original file* 

*for testing and it is design to classify triangle*

*@author: Rongda Kang*

*Summary: The primary goal of this file is to demonstrate a simple python program and learn*

*How to wirte the unittest in away is well formated*

*I am here to Pledge that all of the assignment is done by myself*

*Detail: I mad a lot of changes*

*"""*


| **Test ID**                 | **Input**   | **Expected Results** | **Actual Result** | **Pass or Fail** |
| :-------------------------- | ----------- | -------------------- | ----------------- | ---------------- |
| TestInvalidInput_01         | 1,0,3       | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_02         | 1,3,0       | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_03         | 0,3,1       | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_04         | 201,1,3     | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_05         | 1,201,3     | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_06         | 1,3,201     | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_07         | a,1,1       | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_08         | 1,a,1       | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_09         | 1,1,a       | InvalidInput         | InvalidInput      | Pass             |
| TestNotATriangle_01         | 1,1,3       | NotATriangle         | NotATriangle      | Pass             |
| TestNotATriangle_02         | 3,1,1       | NotATriangle         | NotATriangle      | Pass             |
| TestNotATriangle_03         | 1,3,1       | NotATriangle         | NotATriangle      | Pass             |
| testRightTriangle_01        | 3,4,5       | Right                | Right             | Pass             |
| testRightTriangle_02        | 5,3,4       | Right                | Right             | Pass             |
| testRightTriangle_03        | 3,5,4       | Right                | Right             | Pass             |
| testIsocelesTriangle_01     | 2,1,1       | Isoceles             | Isoceles          | Pass             |
| testIsocelesTriangle_02     | 1,2,1       | Isoceles             | Isoceles          | Pass             |
| testIsocelesTriangle_03     | 1,1,2       | Isoceles             | Isoceles          | Pass             |
| testScaleneTriangles_01     | 2,3,4       | Scalene              | Scalene           | Pass             |
| testScaleneTriangles_02     | 2,4,3       | Scalene              | Scalene           | Pass             |
| testScaleneTriangles_03     | 4,3,2       | Scalene              | Scalene           | Pass             |
| testEquilateralTriangles_01 | 1,1,1       | 'Equilateral'        | 'Equilateral'     | Pass             |
| testEquilateralTriangles_02 | 100,100,100 | 'Equilateral'        | 'Equilateral'     | Pass             |



Result:

```
PS C:\Users\Administrator\Downloads\HW02a> & C:/Users/Administrator/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/Administrator/Downloads/HW02a/TestTriangle-1.py
=*=*=*= Rongda Kang =*=*=*=
=*=*=*= Course 2023S-SSW567-WS =*=*=*=
=*=*=*= Assignment Name: HW-02a Testing Lagacy Porgram =*=*=*=
=*=*=*= 2023-02-10 23:50:13.917572 function was called =*=*=*=


Running unit tests
.......................
----------------------------------------------------------------------
Ran 23 tests in 0.001s

OK
PS C:\Users\Administrator\Downloads\HW02a>

```

