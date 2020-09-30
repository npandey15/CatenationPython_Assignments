Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=1+2j
>>> type(x)
<class 'complex'>
>>> var=int(x)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    var=int(x)
TypeError: can't convert complex to int
>>> # we can't convert complex into any other data type