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

dir_to_save = os.getcwd() + '/threads/'

# hltv_parser.set_url("https://www.hltv.org/forums/threads/2488634/your-16-personality-type")
# banned at 11952 requests
# will implement some securities so I don't get banned so soon

# 1. random request timings
random_request_intervals = True

# 2. add google as referer
# added in MrHltvMens

# 3. add random breaks for requests
random_request_breaks = True
random_request_break_chance = 0.4

# thread_counter = 1
thread_counter = 2488636

thread_404_count = 0
thread_500_count = 0
thread_success_count = 0 


while True:
    new_url = "https://www.hltv.org/forums/threads/" + str(thread_counter) + "/thread"
    #new_url = "https://www.hltv.org/forums/threads/1/your-16-personality-type"
    hltv_parser.set_url(new_url)

    try:
        print(fgWhite + '\n---------------------------')
        print(fgWhite + "Trying url:", new_url, end="\t")
        page_data = hltv_parser.get_page_data()

        thread_info = hltv_parser.get_thread_main_text(page_data, debug=False)
        comments = hltv_parser.get_thread_comments(page_data, debug=False)

        thread_info['comments'] = len(comments)
        
        output_file = open(dir_to_save + "thread_" + str(thread_counter) + ".csv", 'w')

        output_file.write('topic;date;author;flair;flag;text;comments\n')

        util.write_to_file(thread_info, output_file, type='thread')
        util.write_to_file(comments, output_file, type='comments')
        


        # w = csv.writer(open(dir_to_save + "thread_" + str(thread_counter) + ".csv", "w"))
        # for key, val in thread_info.items():
        #     w.writerow([key, val])
        
        # for comment in comments:
        #     for key, val in comment.items():
        #         w.writerow([key, val])
        
        thread_success_count = thread_success_count + 1
        print(fgGreen + 'Success!')

    except Exception as e:
        print(fgRed + 'Failed!')
        print(fgRed + 'Reason:', e)
        if '404' in str(e):
            thread_404_count = thread_404_count + 1
        elif '500' in str(e):
            thread_500_count = thread_500_count + 1

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
                time_off = util.get_random_int(90, 1800)
                print(fgCyan + 'Taking a break for ' + str(time_off) + ' seconds (~' + str(round(time_off/60)) + ' minutes)' )
                print(fgWhite + '----------------------------------')
                print(fgWhite + 'Current thread count:')
                print(fgGreen + 'Succesful thread count: ' + str(thread_success_count))
                print(fgRed + '500 thread count: ' + str(thread_500_count))
                print(fgRed + '404 thread count: ' + str(thread_404_count))
                print(fgWhite + '----------------------------------')

                time.sleep(time_off)        
