import os

try:
    f = open("jsoijisjis.txt")
    print("file not found")
except FileNotFoundError:
    print("file does not exist")