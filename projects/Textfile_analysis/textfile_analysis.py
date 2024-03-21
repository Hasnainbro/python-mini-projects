# -*- coding: utf-8 -*-
import os
import sys
import collections
import string

script_name = sys.argv[0]  # Get the script name from command-line arguments

res = {
    "total_lines": "",
    "total_characters": "",
    "total_words": "",
    "unique_words": "",
    "special_characters": ""
}

try:
    textfile = sys.argv[1]  # Get the input text file from command-line arguments
    with open(textfile, "r", encoding="utf_8") as f:
        data = f.read()  # Read the content of the text file

        # Calculate the number of lines, characters, words, unique words, and special characters
        res["total_lines"] = data.count(os.linesep)  # Count the number of lines
        res["total_characters"] = len(data.replace(" ", "")) - res["total_lines"]  # Count the number of characters (excluding spaces)
        counter = collections.Counter(data.split())  # Count the occurrences of each word
        d = counter.most_common()  # Get the most common words
        res["total_words"] = sum([i[1] for i in d])  # Calculate the total number of words
        res["unique_words"] = len([i[0] for i in d])  # Calculate the number of unique words
        special_chars = string.punctuation  # Get a string containing all special characters
        res["special_characters"] = sum(v for k, v in collections.Counter(data).items() if k in special_chars)  # Count the occurrences of special characters

except IndexError:
    print('Usage: %s TEXTFILE' % script_name)  # Print usage message if no text file is provided
except IOError:
    print('"%s" cannot be opened.' % textfile)  # Print error message if the text file cannot be opened

print(res)  # Print the results
