import os 
# install Termux

os.system('pkg install python2')
os.system('pkg install pip')
os.system('pip install request')
os.system('pip install art')
os.system('pip install colorama')
os.system('pip install time')
print('\aInstall ok!')


from art import *
tprint("Termux","rnd-xlarge")