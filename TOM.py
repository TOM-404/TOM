import os, sys
os.system("git pull")
try:
    __import__("TOM").____tom____()
except Exception as e:
    exit(str(e))
