| **Test ID**                 | **Input**   | **Expected Results** | **Actual Result** | **Pass or Fail** |
| :-------------------------- | ----------- | -------------------- | ----------------- | ---------------- |
| TestInvalidInput_01         | 1,0,3       | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_02         | 1,3,0       | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_03         | 0,3,1       | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_04         | 201,1,3     | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_05         | 1,201,3     | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_06         | 1,3,201     | InvalidInput         | InvalidInput      | Pass             |
| TestInvalidInput_07         | a,1,1       | InvalidInput         | TypeError         | Failed           |
| TestInvalidInput_08         | 1,a,1       | InvalidInput         | TypeError         | Failed           |
| TestInvalidInput_09         | 1,1,a       | InvalidInput         | TypeError         | Failed           |
| TestNotATriangle_01         | 1,1,3       | NotATriangle         | InvalidInput      | Failed           |
| TestNotATriangle_02         | 3,1,1       | NotATriangle         | NotATriangle      | Pass             |
| TestNotATriangle_03         | 1,3,1       | NotATriangle         | NotATriangle      | Pass             |
| testRightTriangle_01        | 3,4,5       | Right                | InvalidInput      | Failed           |
| testRightTriangle_02        | 5,3,4       | Right                | Right             | Pass             |
| testRightTriangle_03        | 3,5,4       | Right                | Right             | Pass             |
| testIsocelesTriangle_01     | 2,1,1       | Isoceles             | InvalidInput      | Failed           |
| testIsocelesTriangle_02     | 1,2,1       | Isoceles             | Isoceles          | Pass             |
| testIsocelesTriangle_03     | 1,1,2       | Isoceles             | Isoceles          | Pass             |
| testScaleneTriangles_01     | 2,3,4       | Scalene              | InvalidInput      | Failed           |
| testScaleneTriangles_02     | 2,4,3       | Scalene              | Scalene           | Pass             |
| testScaleneTriangles_03     | 4,3,2       | Scalene              | Scalene           | Pass             |
| testEquilateralTriangles_01 | 1,1,1       | 'Equilateral'        | InvalidInput      | Fail             |
| testEquilateralTriangles_02 | 100,100,100 | 'Equilateral'        | 'Equilateral'     | Pass             |

```
PS C:\Users\Administrator\Downloads\HW02a> & C:/Users/Administrator/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/Administrator/Downloads/HW02a/TestTriangle-1.py
=*=*=*= Rongda Kang =*=*=*=
=*=*=*= Course 2023S-SSW567-WS =*=*=*=
=*=*=*= Assignment Name: HW-02a Testing Lagacy Porgram =*=*=*=
=*=*=*= 2023-02-10 23:46:36.675128 function was called =*=*=*=


Running unit tests
FF......EEEFFFFFFFFFFFF
======================================================================
ERROR: testInvalidInput_07 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 42, in testInvalidInput_07
    self.assertEqual(classifyTriangle('a',1,1),'InvalidInput','a,1,1 is not a triangle')
  File "c:\Users\Administrator\Downloads\HW02a\TriangleA.py", line 31, in classifyTriangle
    if a > 200 or b > 200 or c > 200:
TypeError: '>' not supported between instances of 'str' and 'int'

======================================================================
ERROR: testInvalidInput_08 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 44, in testInvalidInput_08
    self.assertEqual(classifyTriangle(1,'a',1),'InvalidInput','1,a,1 is not a triangle')
  File "c:\Users\Administrator\Downloads\HW02a\TriangleA.py", line 31, in classifyTriangle
    if a > 200 or b > 200 or c > 200:
TypeError: '>' not supported between instances of 'str' and 'int'

======================================================================
ERROR: testInvalidInput_09 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 46, in testInvalidInput_09
    self.assertEqual(classifyTriangle(1,1,'a'),'InvalidInput','1,1,a is not a triangle')
  File "c:\Users\Administrator\Downloads\HW02a\TriangleA.py", line 31, in classifyTriangle
    if a > 200 or b > 200 or c > 200:
TypeError: '>' not supported between instances of 'str' and 'int'

======================================================================
FAIL: testEquilateralTriangles_01 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 84, in testEquilateralTriangles_01
    self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
AssertionError: 'InvalidInput' != 'Equilateral'
- InvalidInput
+ Equilateral
 : 1,1,1 should be equilateral

======================================================================
FAIL: testEquilateralTriangles_02 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 86, in testEquilateralTriangles_02
    self.assertEqual(classifyTriangle(100,100,100),'Equilateral','100,100,100 should be equilateral')
AssertionError: 'InvalidInput' != 'Equilateral'
- InvalidInput
+ Equilateral
 : 100,100,100 should be equilateral

======================================================================
FAIL: testIsocelesTriangle_01 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 67, in testIsocelesTriangle_01
    self.assertEqual(classifyTriangle(2,3,3),'Isoceles','2,3,3 should be isoceles')
AssertionError: 'InvalidInput' != 'Isoceles'
- InvalidInput
+ Isoceles
 : 2,3,3 should be isoceles

======================================================================
FAIL: testIsocelesTriangle_02 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 69, in testIsocelesTriangle_02
    self.assertEqual(classifyTriangle(3,2,3),'Isoceles','3,2,3 should be isoceles')
AssertionError: 'InvalidInput' != 'Isoceles'
- InvalidInput
+ Isoceles
 : 3,2,3 should be isoceles

======================================================================
FAIL: testIsocelesTriangle_03 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 71, in testIsocelesTriangle_03
    self.assertEqual(classifyTriangle(3,3,2),'Isoceles','3,3,2 should be isoceles')
AssertionError: 'InvalidInput' != 'Isoceles'
- InvalidInput
+ Isoceles
 : 3,3,2 should be isoceles

======================================================================
FAIL: testNotaTriangle_01 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 50, in testNotaTriangle_01
    self.assertEqual(classifyTriangle(1,1,3),'NotATriangle','1,1,3 is NotATriangle')
AssertionError: 'InvalidInput' != 'NotATriangle'
- InvalidInput
+ NotATriangle
 : 1,1,3 is NotATriangle

======================================================================
FAIL: testNotaTriangle_02 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 52, in testNotaTriangle_02
    self.assertEqual(classifyTriangle(3,1,1),'NotATriangle','3,1,1 is NotATriangle')
AssertionError: 'InvalidInput' != 'NotATriangle'
- InvalidInput
+ NotATriangle
 : 3,1,1 is NotATriangle

======================================================================
FAIL: testNotaTriangle_03 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 54, in testNotaTriangle_03
    self.assertEqual(classifyTriangle(1,3,1),'NotATriangle','1,3,1 is NotATriangle')
AssertionError: 'InvalidInput' != 'NotATriangle'
- InvalidInput
+ NotATriangle
 : 1,3,1 is NotATriangle

======================================================================
FAIL: testRightTriangle_01 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 59, in testRightTriangle_01
    self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
AssertionError: 'InvalidInput' != 'Right'
- InvalidInput
+ Right
 : 3,4,5 is a Right triangle

======================================================================
FAIL: testRightTriangle_02 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 61, in testRightTriangle_02
    self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
AssertionError: 'InvalidInput' != 'Right'
- InvalidInput
+ Right
 : 5,3,4 is a Right triangle

======================================================================
FAIL: testRightTriangle_03 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 63, in testRightTriangle_03
    self.assertEqual(classifyTriangle(3,5,4),'Right','3,5,4 is a Right triangle')
AssertionError: 'InvalidInput' != 'Right'
- InvalidInput
+ Right
 : 3,5,4 is a Right triangle

======================================================================
FAIL: testScaleneTriangles_01 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 76, in testScaleneTriangles_01
    self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be scalene')
AssertionError: 'InvalidInput' != 'Scalene'
- InvalidInput
+ Scalene
 : 2,3,4 should be scalene

======================================================================
FAIL: testScaleneTriangles_02 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 78, in testScaleneTriangles_02
    self.assertEqual(classifyTriangle(2,4,3),'Scalene','2,4,3 should be scalene')
AssertionError: 'InvalidInput' != 'Scalene'
- InvalidInput
+ Scalene
 : 2,4,3 should be scalene

======================================================================
FAIL: testScaleneTriangles_03 (__main__.TestTriangles)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\Administrator\Downloads\HW02a\TestTriangle-1.py", line 80, in testScaleneTriangles_03
    self.assertEqual(classifyTriangle(4,3,2),'Scalene','4,3,3 should be scalene')
AssertionError: 'InvalidInput' != 'Scalene'
- InvalidInput
+ Scalene
 : 4,3,3 should be scalene

----------------------------------------------------------------------
Ran 23 tests in 0.003s
```

