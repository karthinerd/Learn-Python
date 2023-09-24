# RegEx - Regular Expression, is a sequence of characters that forms a search pattern

# Used to check if a string contains the specified search pattern

import re

txt = "hi karthi boy"

x = re.search("^h.*y", txt)

if x : print("Yes")

st = "rain in spain"

f = re.findall('ai',st)

print(f)

s = re.split("/s",st)

print(s)