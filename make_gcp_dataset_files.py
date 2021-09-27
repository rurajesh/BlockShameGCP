#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:15:10 2021

@author: rr
---------------------
From each labelled tweet create a file under label directory.
For GCP Automl dataset format. 
"""
import os
import sys

def write_file_in_dir(fnpath,contents):
    '''
    '''
    with open(fnpath, 'w', encoding='utf-8') as ft:
        ft.write(contents)
        
        


labels = [1,2,3,4,5,10,11]
dir_pref = 'data'
labelled_file= 'labeled-all-events-shame-non-shame-1943.txt'
output_dir= 'data/output'

# create dirs for each label
for label in labels:
    os.mkdir(os.path.join(output_dir,str(label)))
#file names prefix
fn='tweet'
i=0
with open(os.path.join(dir_pref,labelled_file),'r') as f:
    for tweet_and_label in f:
        tweet_and_label_l = tweet_and_label.split()
        t, l = ' '.join(tweet_and_label_l[:-1]), tweet_and_label_l[-1]
        fn_path = os.path.join(output_dir, l, fn+str(i))
        i=i+1
        write_file_in_dir(fn_path,t)     