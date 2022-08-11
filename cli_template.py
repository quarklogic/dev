#!/usr/bin/env python3

import sys
import argparse
import os.path
import subprocess
import shutil
import re
import logging

def process_args():
    ''' Setup the argparse configuration for command line options'''

    parser = argparse.ArgumentParser(description='Command Line Script Template')
    parser.add_argument('--log', type=str, help='Specify the log file')
    parser.add_argument('--v', action='store_true', 
                        help='Verbose mode, typically for debugging')

    return parser

def set_logging():
    ''' Setup logging configuration '''

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if args.v:
        logger.setLevel(logging.DEBUG)

    if (args.log):
        fileHandler = logging.FileHandler(args.log)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)


    streamHandler = logging.StreamHandler(sys.stdout)
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)

    logger.info("Starting logger")

    return logger

def system_cmd(cmd):
    ''' Execute system command 
        Usage example: system_cmd(['ls','-l','/tmp'])

        Returns: cmdprocess object use. output.stdout
    '''
    logger.info(f"[system_cmd()] cmd: {cmd}")

    cmd_output = subprocess.run(cmd, text=True, 
                                capture_output=True, check=True)

    return cmd_output


if __name__ == "__main__":

    ## Parse the command line options
    parser = process_args()
    args   = parser.parse_args()

    logger = set_logging()

    ls_output = system_cmd(['ls', '-l', '/tmp'])
    print(f"ls -l /tmp\n {ls_output.stdout}")







