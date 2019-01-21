#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: James Hou
"""
import os
import boto3

# from a folder
def download_files_from_S3(bucket_name, folder_of_interest):
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket_name)
    
    objs = my_bucket.objects.filter(Prefix=folder_of_interest)
    i=0
    for obj in objs:
        fname = obj.key
        if fname.endswith('.mat'):
            i= i+1
            print(fname)
            try:
                os.system('mkdir data_from_s3')
                dest_name = './data_from_s3/' + os.path.basename(fname)
                my_bucket.download_file(fname, dest_name )
            except:
                print("Download failed.")
    print("The total number of files downloaded from S3 is : ", i)
    
    
def upload_file_to_S3(bucket_name, folder_of_interest, file_to_be_uploaded):    
    s3 = boto3.resource('s3')
    
    bucket_name = bucket_name
    prefix = folder_of_interest 

    dest_name = prefix +  os.path.basename(file_to_be_uploaded)
    try:
        s3.Bucket( bucket_name ).upload_file(file_to_be_uploaded, dest_name)
    except:
        print("Upload failed.")       
    
    print('File was succesfully uploaded.')