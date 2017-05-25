from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
from crawlerfileobj import FileHandler

"""
Version: 1.1
Author: NULL

Changes:
    1) File object handled seperately rather than using the crawl function
    2) Implemetation using OOP (classes) for flexible code reuse
    3) Using OOP methodology, we will be able to implement more robust crawler
    
"""

class  Crawler(FileHandler):
    def __init__(self, *args):
        'constructor super class in crawlerfileobj.py'
        super(Crawler, self).__init__()

    def check_links(self, url):
        self.relative_link = ""     #+ init to empty string at every call to check_link()
        self.use_relative_link = False      #+ does not hurt to re-init
        if url[0] == '/':
            'relative link active'
            self.use_relative_link = True
            # + DEBUG
            print("[RL]: ", url + " " + self.relative_link)
            self.relative_link = self.base_url + url
        else:
            self.use_relative_link = False
            #pass
        #+ check if url has already been checked and added to possible_link
        #+...if a match is found, skip to next link
        if url in self.possible_link:  # + url is already checked
            #+ DEBUG
            self.duplicates += 1
            print(url + "\t-> Already checked. Continue...:", self.duplicates)
            pass
        else:
            try:
                if self.use_relative_link:
                      #+ Now check if its alive
                    if requests.get(self.relative_link):
                        self.good_links += 1
                        print (self.relative_link + "\t\t-> [RL]-> Valid: ", self.good_links )
                        return True
                    else:
                        self.bad_links += 1
                        print(self.relative_link + "\t\t-> [RL]-> Bad Link. Discarding...:", self.bad_links)
                        return False
                else:       #+ no relative link [RL]
                    if requests.get(url):
                        self.good_links += 1
                        print (url + "\t\t-> Valid: ", self.good_links )
                        return True
                    else:
                        self.bad_links += 1
                        print(url + "\t\t-> Bad Link. Discarding...:", self.bad_links)
                        return False
            except:
                return False

    def check_link(self, url):
        try:
            if requests.get(str(url)):
                self.good_links += 1
                return True
            else:
                self.bad_links += 1
                return False
        except:
            self.bad_links += 1
            return  False
            pass


    #+ All you do is crawl. No more file handlings. Just crawl
    def crawl(self, url):
        self.base_url = url
        self.link_counter = 0
        #+ NOT original author of this section of code. (copied from stack overflow) #+
        resp = requests.get(url)
        http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
        html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
        encoding = html_encoding or http_encoding
        soup = BeautifulSoup(resp.content, 'html.parser', from_encoding=encoding)
        #######+ END +###############################################
        for link in soup.find_all('a', href=True):
            self.temp_relative_link = ""  # + always reset
            if  self.check_link(link['href']):
                #+ DEBUG
                list(set(self.possible_link))  # + attempt to remove duplicates
                print(link['href'] + " is Valid link. Adding to list...")
                self.possible_link.append(link['href'])         #+ add everything. Processing later
            elif link['href'].startswith('/') or link['href'].startswith(' '):       #+ possible relative ??
                self.temp_relative_link = self.base_url + str(link)
                self.temp_relative_link.strip()
                if self.check_link(self.temp_relative_link):     #+ live now ??
                    #+ DEBUG
                    print(self.temp_relative_link + " Valid after concat. Adding to list...")
                    list(set(self.possible_link))  # + attempt to remove duplicates
                    self.possible_link.append(self.temp_relative_link)
                    self.temp_relative_link = ""        #+ reset
                else:       #+ still bad after concat... :(
                    #+ DEBUG
                    print(self.temp_relative_link + " Bad even after concat. Discarding...")
                    self.temp_relative_link = ""        #+ reset
            else:       #+ still bad ??
                #+ DEBUG
                print(link['href'] + " link cannot be determined. Sorry :(")
                pass



    #+ Call this display_log for debug purposes
    def display_log(self):
        print("\n\n\t\t-------: Displaying all retrieved data :----------\n")
        for x in self.final_link_list:
            print(x + "\n")
        # + DEBUG
        #+ check if an url was supplied
        if self.base_url == "":      #+ empty link
            print("\t\t____---: No url supplied to display log :---____")
        else:
            print("\t-------------------------------------------------------------------------")
            print("\n\t\t___----: LOG RESULT FOR :", self.base_url)
            print("\n\n\t\t:> Number of data written to file: ", self.links_in_file)
            print("\t\t:> Number of duplicates: ", self.duplicates)
            print("\t\t:> Number of bad links: ", self.bad_links)
            print("\t\t:> Number of good links: ", self.good_links)
            print("\n\t\t___----: END LOG RESULT FOR :", self.base_url)
            print("\t-------------------------------------------------------------------------")
