#!/usr/bin/python3

import argparse
import sys
import re
import os.path

def process_file(filename):

    word_count      = 0
    sentence_count  = 0
    character_count = 0

    ## Open up file for reading
    contents = open(filename, 'r')

    ## Loop through contents of file
    for line in contents:
        line = line.rstrip('\n')

        print(f"LINE: {line}")

        ## Split line into words
        words = line.split()

        for word in words:
            word_count += 1

            ## Get number of characters in word
            word_length = len(word)

            ## Increment character counter
            character_count += word_length

            print(f"word: {word} length: {word_length}")

            ## Search for end of sentence markers: .!?
            if re.search(r'[\.\?\!]$', word):
                print(f"  found end of sentence")
                sentence_count += 1

        print("\n")

    return [word_count, sentence_count, character_count]

def autoread_method(stats):
    word_count      = stats[0]
    sentence_count  = stats[1]
    character_count = stats[2]

    readindex = 4.71 * (character_count / word_count) + \
                0.5 * (word_count / sentence_count) - 21.43

    return readindex


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--index', type=str, 
        default="autoread")

    args = parser.parse_args()

    ## Check if --file exists before processing it
    if (os.path.exists(args.file)) is False:
        print(f"ERROR: File ({args.file}) does not exist!")
        exit()

    stats = process_file(args.file)

    readindex = autoread_method(stats)

    print(f"read Index: {readindex}")




