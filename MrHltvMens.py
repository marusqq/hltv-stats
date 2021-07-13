#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"

"class made for requesting to hltv"

import urllib.request
from bs4 import BeautifulSoup


class MrHltvMens:

    def __init__(self):
        self.user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
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

    def get_thread_main_text(self, soup, debug=False, comment=False):
        
        if not comment:
            data = soup.find_all(class_="forum-topbar")[0]
            topic = data.find(class_="topic").text
            reformatted_topic = topic.replace('\n', '')

            if debug:
                print('Topic:', reformatted_topic)

        if comment:
            data = soup        

        author = data.find(class_="authorAnchor").text.strip()

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

        if flair:
            flair = flair.replace("fan of ", "")
        else:
            flair = 'None'

        if debug:
            print('Flair:', flair)

        flag = data.find(class_="flag")['title']
        
        if debug:
            print('Flag:', flag)

        text = soup.find_all(class_="forum-middle")[0].text.strip()
        reformatted_text = "\\n".join(text.splitlines())

        if debug:
            print('???????:', reformatted_text)
            

        date = soup.find(class_="forum-bottombar").text.strip()

        if debug:
            print('Date:', date)

        if not comment:

            result_dict = {
                "topic" : reformatted_topic,
                "date" : date, 
                "author" : author,
                "flair" : flair,
                "flag" : flag,
                "text" : reformatted_text
            }

        else:

            result_dict = {
                "date" : date,
                "author" : author,
                "flair" : flair,
                "flag" : flag,
                "text" : reformatted_text
            }


        return result_dict

    def get_thread_comments(self, soup, debug=False): 

        comments = []
        comments_soup = soup.find_all(class_="post")

        if debug:
            print('Comments in soup:', comments_soup)

        for comment_soup in comments_soup:
            if debug:
                print('Sending comment to self.get_thread_main_text:', comment_soup)
            comment = self.get_thread_main_text(comment_soup, comment=True)
            comments.append(comment)
            
        return comments


#url = "https://www.hltv.org/forums/threads/2488634/your-16-personality-type#r50236990"
