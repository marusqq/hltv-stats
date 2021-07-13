from MrHltvMens import MrHltvMens
import os, csv, time

hltv_parser = MrHltvMens()

fgRed = "\033[31m"
fgWhite = "\033[37m"
fgGreen = "\033[32m"

dir_to_save = os.getcwd() + '/tests/'

# hltv_parser.set_url("https://www.hltv.org/forums/threads/2488634/your-16-personality-type")
# #hltv_parser.set_url("https://www.hltv.org/forums/threads/2488612/your-16-personality-type")
# hltv_parser.set_url("https://www.hltv.org/forums/threads/2488111/spirit-vs-gambit")

thread_counter = 1

while True:
    new_url = "https://www.hltv.org/forums/threads/" + str(thread_counter) + "/thread"
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
        time.sleep(1)
