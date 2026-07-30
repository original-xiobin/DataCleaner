#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:21:07 2026

@author: xiobin
"""


from data_utils.cleaner_utils import CleanerUtils
import argparse


def main():
    utils = CleanerUtils(argparse.ArgumentParser(
        description="Clean input data."))
    utils.clean_data()

    
if __name__ == "__main__":
    main() 
            