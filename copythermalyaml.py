#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:56:58 2023

@author: wojtekgierlotka
"""

import os
import shutil

def copy_thermalyaml(number_dir,number_negative):
    current_dir = os.getcwd()
    number_yaml=-1*number_negative
    for dir in range(1,number_dir+1):
        try:
            file_to_copy = current_dir+'/'+str(dir)+'/thermal_properties.yaml'
            file_dest = current_dir+'/thermal_properties.yaml-'+str(number_yaml)
            shutil.copy(file_to_copy,file_dest)
        except:
            print('There was an error when copying thermal_properties.yaml. Check your subfolders.')
        number_yaml=number_yaml+1
    try:
        file_to_copy = current_dir+'/thermal_properties.yaml'
        file_dest = current_dir+'/thermal_properties.yaml-0'
        shutil.copy(file_to_copy,file_dest)
    except:
        print('Error. Check whether there is thermal_properties.yaml in your main folder')
            