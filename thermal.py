#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 19:04:41 2023

@author: wojtekgierlotka
"""
import os
def calc_thermal(number_dir,number_disp):
    current_dir = os.getcwd()
    for dir in range(1,number_dir+1):
        os.chdir(current_dir+'/'+str(dir))
        phonopy_command ="phonopy -f "
        i=1
        for number in range(number_disp):
            x1 = int(i)
            nsv = str(x1).zfill(3)
            phonopy_command=phonopy_command+"disp-"+nsv+"/vasprun.xml "
            i = i+1
        try:
            os.system(phonopy_command)
        except:
            print('There was an error')
        phonopy_command='phonopy -t mesh.conf'
        try:
            os.system(phonopy_command)
        except:
            print('There was an error2')
        
