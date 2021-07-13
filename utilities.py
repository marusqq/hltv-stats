#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"

import random

def get_random_int(min=1, max=20):
    return random.randint(min, max)

def write_to_file(data, out_file, type="thread"):
    
    if type == "comments":

        for entry in data:
            
            csv_entry = 'none;' + \
                entry['date'] + ';' + \
                entry['author'] + ';' + \
                entry['flair'] + ';' + \
                entry['flag'] + ';' + \
                entry['text'] + ';none;'

            out_file.write(csv_entry + '\n')


    elif type == "thread":

        csv_entry = data['topic'] + ';' + \
                data['date'] + ';' + \
                data['author'] + ';' + \
                data['flair'] + ';' + \
                data['flag'] + ';' + \
                data['text'] + ';' + \
                str(data['comments']) + ';'

        out_file.write(csv_entry + '\n')

    return