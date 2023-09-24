from greet_module import greet as welcome

import greet_module

import platform

userName = input("What is Your Name ?\n")

welcome(userName)

greet_module.greet(userName)

# PLATFORM

x = platform.system()

print(x)

print(dir(platform))