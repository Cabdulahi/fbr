#!/usr/bin/python
# coding=utf-8
#///.coded by cabdulahi sharif
import time
import os,sys
from my import see
from my import fbreport
from my import fbbrute
os.system("clear")

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

green = '\033[32;1m'

gta = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
  #//Colors 
white = '\033[1;37m' # White 
red = '\033[31m' # red
orange = '\033[33m' # orange
blue = '\033[34m' # blue
p  = '\033[35m' # purple
C  = '\033[36m' # cyan

idgroup = []


idd = ("100022350489847")
duma = ("===========================================")
savefile = ("id.txt")
banner= C+p+"""


 
             __ _
            / _| |__  _ __
           | |_| '_ \| '__|
           |  _| |_) | |    #Version 0.2
           |_| |_.__/|_|    @New Update 0.3
              
          [FBR Facebook Hacking Tool]
        [@Created By Cabdualahi Sharif]      """+C+p+"""
             Youtube Channel: Somali4You
             Facebook: cabdulahi.sharif.100 ------------------------------------------"""
print banner
me = (C+p+'[💡]Cabdulahi=>> ')
oh= time.sleep(1)


class fbr:
 def __init__(self):
     oh
     print (white+'  <{(1))>'+green+' Facebook Reporter')
     oh
     print (white+'  <{(2))>'+green+' Facebook Pishing Attack')
     oh
     print (white+'  <{(3))>'+green+' Facebook Bruteforce Attack')
     oh
     print (white+'  <{(4))>'+green+' Check Update')
     oh
     print (white+'  <{(0))>'+green+' GoodBye')
     time.sleep(2)
     print
     print
     self._check()




 def _check(self):
     try:
         inn = raw_input(me+(''))
         if(inn=='1'):
             print
             self.updown()
             print g
         elif(inn=='2'):
                 print
                 see.home()
         elif(inn=='3'):
             print 
             fbbrute.shit()
         elif(inn=='4'):
             time.sleep(2)
             exit()
         elif(inn=='0'):
             exit()
     except Exception as g:
          print g
     else:
         return self._check()
 
       
       
 def updown(self):
     oh
     print (white+'  <{(1))>'+green+'  Custom Id')
     oh
     print (white+'  <{(2))>'+green+'  list Ids')
     print (white+'  <{(0))>'+green+'  Back')
     print
     inn2 = raw_input(me+(''))
     if(inn2=='1'):
         fbreport.fbr()
     elif(inn2=='2'):
         print (red+'[⚠]Update Not available')
         exit()
     elif(inn2=='0'):
         os.system('clear')
         os.system('python2 fbr.py')
     else:
         return self.updown()
     
       
       

       
if __name__ == "__main__":
	fbr()