Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=6
>>> y=10
>>> 
>>> Resultname=x
>>> x=y
>>> y=Resultname
>>> print("The value of x after swapping: {}".format(x))
The value of x after swapping: 10
>>> print("The value of y after swaaping:{}".format(y))
The value of y after swaaping:6
>>> 
>>> 
>>> # without using third variable
>>> 
>>> x=6
>>> y=10
>>> 
>>> x,y=y,x
>>> print("x=",x)
x= 10
>>> print("y=",y)
y= 6
>>> 