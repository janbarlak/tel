# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 07:41:39 2019

@author: barlak
"""

import fire
import os

def cislo(string):
    script_dir = os.path.dirname(__file__)
    f_path = os.path.join(script_dir,"contacts")
    #f = open("C:\\Users\\barlak\\bin\\contacts","r")
    f = open(f_path,"r")
    lines=f.readlines()
    
    zoznam={}
    for n,line in enumerate(lines):
    #    print(line)
        if "KlapkaT:" in line:
            value=line.split(":")[1].strip()
        if "MenoSort:" in line:
            key=line.split(":")[1].strip()
            zoznam[key] = value
    #    if n>500: break
    f.close()

    
    l = [[key,value] for key, value in zoznam.items() if string in key.lower()]
    for i,item in enumerate(l):
        print(', '.join(l[i]))

if __name__=='__main__':
    fire.Fire(cislo)

