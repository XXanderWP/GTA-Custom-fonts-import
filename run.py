#!/usr/bin/python

import sys
import os
import time

if len(sys.argv) == 1:
    print('Please enter name of font file')
    exit()
fontFile = sys.argv[1].replace(".ttf", "")
print('Selected font: '+fontFile)
if not os.path.isfile('./'+fontFile+'.ttf'):
    print('File ./'+fontFile + '.ttf not exist')
    exit()

with open('./default.xml') as f:
    contents = f.read()
    contents = contents.replace("{{name}}", fontFile)
    with open(fontFile+'.xml', 'w') as f:
        f.write(contents)
        f.close()
        print('Create XML config')
        # time.sleep(0.5)

        os.system('.\swfmill.exe simple '+fontFile+'.xml '+fontFile+'.swf')
        # time.sleep(1)
        os.system('.\gfxexport.exe '+fontFile+'.swf')

        os.remove('./'+fontFile+'.xml')
        os.remove('./'+fontFile+'.swf')
        print('###############################')
        print(fontFile+'.gfx created. GLFH <3')
        print('###############################')
