#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 23:22:38 2026

@author: rikuruotsalainen
"""

import os
from datetime import datetime as dt
import argparse
import tkinter

class CleanerUtils:
    input_path = ""
    output_path = os.getcwd()
    ct = dt.now()
    timestr = str(ct.date()) + "-" + str(ct.hour) + str(ct.minute)
    filename = f"result_{timestr}.csv"
    summary = f"summary_{timestr}.txt"
    
    def __init__(self, args):
        self.process_arguments(args)
        
    
    def process_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("-i", "--input_path", type=str, 
                            help="Define an input file path for the file that" 
                            + "needs data cleaning.\n" + 
                            "Include the file name\nExamples:\n" +
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
        parser.add_argument("-n", "--filename", type=str, 
                            help="Define desired" +
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
            
            
    def clean_data(self):
        print("Cleaning data from the input file: " + self.input_path)
        print("The output files " + self.filename + " and " + self.summary + 
              " are saved to the following folder " + 
              self.output_path)

    def select_path(self, tk: tkinter, button: str, entry: tkinter.Entry):
        directory = tk.filedialog.askdirectory()
        