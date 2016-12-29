#!/usr/bin/env python

import subprocess

# Example on how to use this script.
# ./tellWords.py [ and press enter]
# In the prompt line type what you want and press enter again.

command = "say"

text = raw_input("Enter word or a sentence and press enter: ")

characters = list(text)

for c1 in characters:
  if c1 == " ":
    subprocess.call([command, ",,"])
  else:
    subprocess.call([command, c1])

subprocess.call([command, text])

