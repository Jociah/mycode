#!/usr/bin/env python3

# standard library imports
import shutil # shell utilities will be used to move files
import os # provides access to low level os operation (agnostic to flavor of OS)

def main():
    """caled at runtime"""
    #This will allow the user to run the porgram from any location on the system.
    os.chdir('/home/student/mycode/')
    shutil.move('raynor.obj', 'ceph_storage/') # try moving the file raynor.obj

# Prompt the user for a new name for the kerrigan.obj file.
xname = input('What is the new name for kerrigan.obj? ') #collect string input from the user

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # moving kerrigan.obj into

main() # this calls our main function
