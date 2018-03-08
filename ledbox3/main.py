# -*- coding: utf-8 -*-

"""Main module."""
import sys
import click
import urllib.request
import argparse 
import requests 
from urllib.request import urlopen
import os


def read_file(input_link):
    '''Function which reads in a file from a URL or local file and returns the
    contents of the file in a string'''
    if input_link.startswith('http'):
        
        req = urllib.request.urlopen(input_link)
        text = req.read().decode('utf-8')
        print(text)
        print ("File has been read Eoin!")
        
    else:
        if not os.path.isfile(input_link):
            print('File does not exist.')
            print ("you need to fix here!")
        
        
        else: 
            text =open(link,'r').read() #.read() converts to a string
            print ("What am i doing here")
    return text





'''


#argparse stuff
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument("-i", "--input", action="store_true")
#group.add_argument("-f", "--file", action="store_true")

parser.add_argument("source", help="a valid url")
args = parser.parse_args()




def read_file(filename):
    """Function to read a file and process the contents"""
    if filename.startswith("http"):
        req = urllib.request.urlopen(filename)
        line =req.read().decode('utf-8')
        print ("File has been read")
        return line
    else:
        if not os.path.isfile(filename):
            print('File does not exist.')
        else:
        # Open the file for reading as a string
            line = open(filename, 'r').read()
            return line
'''''

def main():
        file_input = read_file(sys.argv[2])
        if len(sys.argv) < 3:
            print( file_input, "\nCheck the parameters, no file given.\nInput should be of form 'led_checker --input file_link'")
            
        else:
            file= read_file(file_input)
            print ("succesfully read!")
        
                                                    
if __name__ == "__main__":
    main()