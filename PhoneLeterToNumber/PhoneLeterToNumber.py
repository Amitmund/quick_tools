#/usr/bin/env python
import sys

# usage: python ScriptName OnlyOneArg
# Example: python ScriptName agenda

# Want to get the number if I give a telephone character

dict = {'a':2, 'b':2, 'c':2, 'd':3, 'e':3, 'f':3, 'g':4, 'h':4, 'i':4, 'j':5, 'k':5, 'l':5, 'm':6, 'n':6, 'o':6, 'p':7, 'q':7, 'r':7, 's':7, 't':8, 'u':8, 'v':8, 'w':9, 'x':9, 'y':9, 'z':9, '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 } 


#name = raw_input ('Provide the name: ')
name = sys.argv[1]
a_name = list(name)

value = ""
for char in a_name:
  value += str((dict[char]))
print (value)
