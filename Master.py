import pathlib as path
import os
import sys
import io
import hashlib



files = ["%s/%s" % ("C:/Users/desmo/Desktop/Source", i) for i in os.listdir("C:/Users/desmo/Desktop/Source") if os.path.isfile("%s/%s" % ("C:/Users/desmo/Desktop/Source", i))]
print(files)

