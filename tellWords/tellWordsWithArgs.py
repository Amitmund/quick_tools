#!/usr/bin/env python

import subprocess
import sys

# Example on how to use this code:
# ./tellWordsWithArgs.py I like to eat apple

command = "say"

text = sys.argv[1:]

tc = list(text)
topCharacters = list(tc)

for characters in topCharacters:
  c1 = list(characters)
  for c1 in characters:
    if c1 == " ":
      subprocess.call([command, ",,"])
    else:
      subprocess.call([command, c1])

#Changing list to string again.
text=''.join(text)
subprocess.call([command, text])

