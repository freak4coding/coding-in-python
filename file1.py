# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:45:10 2019

@author: dell
"""
import os
f=open("data.txt","r")
#print(f.read(),end="")
#f1=open("data.txt","a")
#f1.write("\nI love the way she react !")
f2=open("newData.txt","w")
for a in f:
    f2.write(a)
f.close()
#f1.close()
f2.close()
#os.renames("newData.txt","myData.txt")
os.remove("myData.txt")
os.