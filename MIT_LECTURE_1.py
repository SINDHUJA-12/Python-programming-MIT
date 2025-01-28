>>> #type() function is to realise the datatype of the data
>>> type(8)
<class 'int'>
>>> type(2.0)
<class 'float'>
>>> type("Data")
<class 'str'>
>>> type(False)
<class 'bool'>
>>> #Type Conversion helps to get the different datatype version of the existing data
>>> float(5)
5.0
>>> int(3.14)
3
>>> round(9.9)
10
>>> float(round(7.3))
7.0
>>> #Expressions are the combination of objects and operator <obj><operator><obj>
>>> (6+9)*(49/7)
105.0
>>> int(5**2*3.14)
78
>>> type(int(3.14)+(4/9))
<class 'float'>
>>> #Division always results in the float
>>> #Floor divison truncates the division
>>> 10//3
3
>>> 10%4 #Modulus results in the remainder
2
>>> #Variables are assigned values <Variable_name>=<Expression\Value>
>>> diagonal_1,diagonal_2=8,12 #Let's calculate the area of the rhombus
>>> area=(1/2)*diagonal_1*diagonal_2 #Variables can be assigned other variables as well
>>> print(area)
48.0
>>> diagonal_1=10 #Rebounding variables to other values
>>> print(area) #Variable's value wouldn't change unless it's calulated again
48.0
>>> area=(1/2)*diagonal_1*diagonal_2
>>> print(area)
60.0
>>> #Swapping two variables
>>> a,b=12,7
>>> a,b=b,a #This multiple assignment can swap variables
print(a)
7
print(b)
12
temp=a #New Variable is used for temporarily storing the value in this method
a=b #a can be altered as this is already stored in temp
b=temp
print(a)
12
print(b)
7
