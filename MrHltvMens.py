#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"

"class made for requesting to hltv"

import urllib.request
from bs4 import BeautifulSoup


class MrHltvMens:

    def __init__(self):
        self.user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
        self.referer = "https://www.google.com/"
        self.url = "https://www.hltv.org/"

    def set_url(self, url):
        self.url = url

    def get_page_data(self):
        req = urllib.request.Request(
	    self.url,
	    data=None,
	    headers=self.user_agent)

        req.add_header('Referer', self.referer)

        html = urllib.request.urlopen(req)
        soup = BeautifulSoup(html, 'html.parser')

        return soup

    def get_thread_main_text(self, soup, debug=False):

        data = soup.find_all(class_="forum-topbar")[0]

        topic = data.find(class_="topic")

        if debug:
            print('Topic:', topic)

        author = data.find(class_="authorAnchor")

        if debug:
            print('Author:', author)

        # for team
        flair = data.find(class_="teamLogo")
        
        if flair:
            flair = flair['title']
        
        if not flair:
            # for a player
            flair = data.find(class_="love")
            if flair:
                flair = flair['title']

        if not flair:
            flair = 'None'

        if debug:
            print('Flair:', flair)

        flag = data.find(class_="flag")
        
        if debug:
            print('Flag:', flag)

        text = soup.find_all(class_="forum-middle")[0]

        if debug:
            print('Text:', text)

        result_dict = {
            "topic" : topic.text,
            "author" : author.text.strip(),
            "flair" : flair,
            "flag" : flag['title'],
            "text" : text.text
        }

        return result_dict

    def get_thread_comments(self, soup):
        return 'test'


#url = "https://www.hltv.org/forums/threads/2488634/your-16-personality-type#r50236990"



#comments = soup.find_all("div", {"class": "post"})

#for comment in comments:
    #print(len(comment))
    #if comment and '>' in comment:
        #post_info = comment.split('>')

        #print(post_info)
        #print(comment)
        #print('------------')
        #input()

#collect_string = False

'''
for strip in strips:
    if '#' in strip and not collect_string:
        collect_string = True

    elif collect_string:
        print(strip)
        collect_string = False
        '''
