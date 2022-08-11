#!/usr/bin/python3

import argparse
import sys
import re
import os.path



if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--index', type=str, default="autoread")

    args = parser.parse_args()

    ## Check if --file exists before processing it
    if (os.path.exists(args.file)) is False:
        print(f"ERROR: File ({args.file}) does not exist!")
        exit()







