#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:01:26 2023

@author: wojtekgierlotka
"""
import os
import shutil

def copy_mesh_band(number_dir):
    src=['mesh.conf','band.conf']
    current_dir = os.getcwd()
    for dir in range(1,number_dir+1):
        for file_name in src:
            try:
                file_dest = current_dir+'/'+str(dir)+'/'+file_name
                file_to_copy = current_dir+'/'+file_name
                shutil.copy(file_to_copy,file_dest)
            except:
                print('There was an error when copying mesh.conf and band.conf')



    
