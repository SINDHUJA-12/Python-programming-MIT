>>> #Strings are a sequence of case sensitive charectors contained within quotes
>>> a="="
>>> b="^"
>>> c='.'
>>> n='2' #Anything within quotes are charectors\string
>>> cat = a+b+int(n)*c+b+a #Concatenation(+) of strings along with repetion(*)
>>> print(cat) #Concatenation combines sevaral strings together without space
=^..^=
>>> print(len(cat)) #Provides the length(number of individual charectors) in string
6
>>> #String operations : String index(charector position) always starts at 0
>>> string = 'Python'
>>> string[0]
'P'
>>> string[1]
'y'
>>> string[5]
'n'
>>> string[-1] #Index of the last element starts at -1 and grows downwards to the first element
'n'
>>> string[-6]
'P'
>>> #Slicing the string results in substring [starting index : stopping index : step value] , step is 1 by default and it decides the number of hops
>>> new = 'We are animals'
>>> new[7:len(new)] #Stop index must be 1 value larger than desired charector index
'animals'
>>> new[-9:-len(new)-1:-1]
'era eW'
>>> new[::-1] #This can reverse the string as it traverses back in -1 hop
'slamina era eW'
>>> #Immutable strings can become the new versions but not modified
>>> new = string + new[2:len(new)]
>>> print(new)
Python are animals
>>> #input() function is able to take in the user inputs in string format
>>> get = input("Get me a string: ")
Get me a string: I _ breakfast yesterday
>>> print(get)
I _ breakfast yesterday
>>> print(get[0:2]+"had"+ get[3:len(get)])
I had breakfast yesterday
#Fstrings contain expression within braces computed at run time
radius=5
pi=3.14
print(f'The circle of radius {radius} gives the area {radius**2*pi}')
The circle of radius 5 gives the area 78.5
#Comparison operators and logical operators
not('and'=='ant') #Equality fails due to difference thus False and logical operator complements the output to True
True
50<-1
False
4>0
True
(50<-1) or (4>0)
True
(50<-1) and (4>0)
False
#if-else conditions are branching in a code executes based on satisfied condition
#Program
Distinction=90
Pass_mark=50
mark=int(input('Enter your mark: '))
if(mark>=Distinction):
    print('Yay,Distinction')
elif(mark>=Pass_mark):
    print('Well,Pass')
else:
    print('Fail,Work hard')
==================== RESTART: C:/Users/Sindhu/MIT/IF-ELSE.py ===================
Enter your mark: 78
Well,Pass