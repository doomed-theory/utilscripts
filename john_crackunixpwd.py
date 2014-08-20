#!/usr/bin/python3
from subprocess import call
import os, sys
import os.path
passwdfile=r"/etc/passwd" # the passwd file to use, defaults to /etc/passwd
shadowfile=r"/etc/shadow" # the shadow file to use, defaults to /etc/shadow
pwdlist=r"/usr/share/password.lst"    #the password dictionary for john to use, defaults to /usr/share/john/password.lst
unshadowfile=r"./unshadowfile.txt" #the file john's unshadow writes to
finalfile=r"./johncracked.txt"
unshadowcmd="unshadow" #the unshadow command, defaults to unshadow. change if john is not in PATH
johncmd="john" #change if john is not in path
if not os.path.isfile(passwdfile):
    passwdfile=input("enter location of passwd file: ")
if not os.path.isfile(shadowfile):
    shadowfile=input("enter location of shadow file: ")
usewdlst=input("would you like to use a wordlist: ")
if os.path.isfile(unshadowfile):
    delyn=input("files already exists. Would you like to delete the file? type y or n: ")
    while True:
        if delyn.startswith('y'):
            os.remove(unshadowfile)
            os.remove(finalfile)
            break
        elif delyn.startswith('Y'):
            os.remove(unshadowfile)
            os.remove(finalfile)
            break
        elif delyn.startswith('n'):
            sys.exit(0)
        elif delyn.startswith('N'):
            sys.exit(0)
        else:
            print("please enter y or n")
            continue
o=open(unshadowfile, "w+")
call([unshadowcmd, passwdfile, shadowfile],stdout=o)
while True:
    if usewdlst.startswith('y'):
        wordlist="--wordlist="+pwdlist
        break
    elif usewdlist.startswith('Y'):
        wordlist="--wordlist="+pwdlist
        break
    elif usewdlist.startswith('n'):
        wordlist=""
        break
    elif usewdlist.startswith('n'):
        wordlist=""
        break
    else:
        continue
#wordlist="--wordlist"+pwdlist
o2=open(finalfile, "w+")
call([johncmd, wordlist, unshadowfile])
call([johncmd, "--show",unshadowfile], stdout=o2)
call([johncmd, "--show",unshadowfile])
o.close()
o2.close()
