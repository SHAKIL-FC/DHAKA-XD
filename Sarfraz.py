#coding=utf-8
import os, sys, platform

os.system('xdg-open https://facebook.com/mdshakilislam.4321/')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf Sarfraz.so Sarfraz32.so')
except:
    pass
os.system('rm -rf Sarfraz.so Sarfraz32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Sarfraz.so'):
        os.system('curl -L https://github.com/Shakil19910/executables/blob/main/Sarfraz.cpython-311.so?raw=true -o Sarfraz.so') 
        import Sarfraz
    else:
        import Sarfraz32