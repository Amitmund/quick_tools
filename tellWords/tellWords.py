#!/usr/bin/env python

import subprocess
command = "say"

text = raw_input("Enter word or a sentence and press enter: ")

characters = list(text)

for c1 in characters:
  if c1 == " ":
    subprocess.call([command, ",,"])
  else:
    subprocess.call([command, c1])

subprocess.call([command, text])

