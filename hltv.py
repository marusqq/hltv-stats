#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"

from MrHltvMens import MrHltvMens
import utilities as util
import os, csv, time

hltv_parser = MrHltvMens()

fgRed = "\033[31m"
fgWhite = "\033[37m"
fgGreen = "\033[32m"
fgCyan = "\033[36m"

dir_to_save = os.getcwd() + '/tests/'

# hltv_parser.set_url("https://www.hltv.org/forums/threads/2488634/your-16-personality-type")
# banned at 11952 requests
# will implement some securities so I don't get banned so soon

# 1. random request timings
random_request_intervals = True

# 2. add google as referer
# added in MrHltvMens

# 3. add random breaks for requests
random_request_breaks = True
random_request_break_chance = 0.08

thread_counter = 11952


while True:
    new_url = "https://www.hltv.org/forums/threads/" + str(thread_counter) + "/thread"
    #new_url = "https://www.9gag.com"
    hltv_parser.set_url(new_url)

    try:
        print(fgWhite + '\n---------------------------')
        print(fgWhite + "Trying url:", new_url, end="\t")
        page_data = hltv_parser.get_page_data()
        thread_info = hltv_parser.get_thread_main_text(page_data, debug=False)

        w = csv.writer(open(dir_to_save + "thread_" + str(thread_counter) + ".csv", "w"))
        for key, val in thread_info.items():
            w.writerow([key, val])
        print(fgGreen + 'Success!')

    except Exception as e:
        print(fgRed + 'Failed!')
        print(fgRed + 'Reason:', e)

    finally:

        thread_counter = thread_counter + 1

        # random request intervals
        if random_request_intervals:
            time_to_wait = util.get_random_int()
        else:
            time_to_wait = 1

        time.sleep(time_to_wait)

        # random breaks
        if random_request_breaks:
            if (random_request_break_chance * 100) > util.get_random_int(1,100):
                time_off = util.get_random_int(900, 3600)
                print(fgCyan + 'Taking a break for ' + str(time_off) + ' seconds (~' + str(round(time_off/60)) + ' minutes)' )
                time.sleep(time_off)
        
