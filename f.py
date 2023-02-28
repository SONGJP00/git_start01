Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='python'
>>> f"{[0:!^12]}".fotmat(a)
SyntaxError: f-string: invalid syntax
>>> f'{0:!^12}'.format(a)
'!!!!!0!!!!!!'
>>> f'{python:!^12}'
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    f'{python:!^12}'
NameError: name 'python' is not defined
>>> f'{a:!^12}'
'!!!python!!!'
