#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 23:22:38 2026

@author: rikuruotsalainen
"""

import os
import argparse

class CleanerUtils:
    input_path = ""
    output_path = os.getcwd()
    filename = "result.txt" 
    
    def __init__(self, args):
        self.process_arguments(args)
    
    def process_arguments(self, parser):
        #parser = argparse.ArgumentParser(description="Clean input data.")
        parser.add_argument("-i", "--input_path", type=str, 
                            help="Define an input file path for the file that" 
                            + "needs data cleaning.\n Include the file name.\n" +
                            "Examples:\n" +
                            "/Users/admin/source/input.txt\n" +
                            "c:\source\input.txt")
        parser.add_argument("-o", "--output_path", type=str, 
                            help="Define an output file path for" + 
                            "the cleaned data file." + 
                            "\nDefault folder is the current working folder." + 
                            "\nDon't include a file name." +
                            "\nDefault file name " +
                            "\nfor the output file is result.txt.\n" +
                            "Examples:\n" +
                            "/Users/admin/source/input.txt\n" +
                            "c:\source\input.txt")
        parser.add_argument("-n", "--filename", type=str, help="Define desired" +
                            " name for the file")
        args = parser.parse_args()
        if (args.input_path == None or args.input_path == "" 
            or not args.input_path.endswith(".csv")):
            print("Please provide a path for the .csv input file!\n" +
                  "Examples:\n" +
                  "/Users/admin/source/input.txt\n" +
                  "c:\source\input.txt")
        else:
            self.input_path = args.input_path
            if args.output_path != os.getcwd() and args.output_path != None:
                self.output_path = args.output_path
            if (args.filename != "result.txt" and args.filename != ""
                and args.filename != None):
                self.filename = args.filename
            # REMOVE THESE
            print("Input type: " + str(type(self.input_path)) + 
                  "\nOutput type: " + str(type(self.output_path)) +
                  "\nOutput filename type: " + str(type(self.filename)))
            # REMOVE UPPER TESTING SECTION
            print("Input path: " + self.input_path + 
                  "\nOutput path: " + self.output_path +
                  "\nFilename: " + self.filename)
            
    def clean_data(self):
        pass