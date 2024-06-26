# File handling

"""
File opening modes:
x : creates a file, gives error if file is already
present

"""

mylist = [ 'line 1\n', 'line2\n', 'line 3\n' ]

with open('file.txt', 'rt') as file:
    print( file.readline() )
    print( file.readline() )
    print( file.readline() )