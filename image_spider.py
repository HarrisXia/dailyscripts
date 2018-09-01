#!/usr/bin/env python
# -*- coding:utf-8 -*-

#...................................
print("keyword:please input....\nform:A+B")
#input keyword
word = input()

#..............................................
import json
import os
import re
import socket
import urllib
import urllib.request
import urllib.parse
import urllib.error
import time

# set fault_time_out
timeout = 5
socket.setdefaulttimeout(timeout)

counter = 1

#.............................................
class Crawler:
    # set time_sleep
    __time_sleep = 0.1
    __amount = 0
    __start_amount=0

    # download_sleep_time
    def __init__(self, t=0.1):
        self.time_sleep = t

    # program start
    def __getImages(self, word=word):
        search = urllib.parse.quote(word)
        # image_num
        pn = 0
        while pn < self.amount:
            global counter
            #headers
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search + '&cg=girl&pn=' + str(
                    self.__start_amount) + '&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
            #deal with errors
            try:
                time.sleep(self.time_sleep)
                req = urllib.request.Request(url=url, headers=headers)
                page = urllib.request.urlopen(req)
                data = page.read().decode('utf8')
            except UnicodeDecodeError as e:
                print('-----UnicodeDecodeErrorurl:', url)
            except urllib.error.URLError as e:
                print("-----urlErrorurl:", url)
            except socket.timeout as e:
                print("-----socket timout:", url)
            else:
                # analyze json
                json_data = json.loads(data)
                self.__saveImage(json_data, word)
                # download next page
                print("download next page")
                pn += 60
            finally:
                page.close()
        print("mission complete!\ntask finish!")
        return

    #................................................
    # save images
    def __saveImage(self, json, word):
        global counter
        # determine whether the folder is dupicated
        if not os.path.exists("./" + word):
            os.mkdir("./" + word)
        #obtain image_length
        counter = len(os.listdir('./' + word)) + 1
        for info in json['imgs']:
            try:
                if self.__downloadImage(info, word) == False:
                    counter -= 1
            except urllib.error.HTTPError as urllib_err:
                print(urllib_err)
                pass
            except:
                time.sleep(1)
                print("Unknown Errors Occur!")
                continue
            else:
                print("target_image+1,already got\n" + str(counter) + "images")
                counter += 1
        return

    #..................................................
    # download images
    def __downloadImage(self, info, word):
        global counter
        time.sleep(self.time_sleep)
        fix = self.__getFix(info['objURL'])
        urllib.request.urlretrieve(info['objURL'], './' + word + '/' + str(counter) + str(fix))

    # get the suffix
    def __getFix(self, name):
#re???????
        m = re.search(r'\.[^\.]*$', name)
        if m.group(0) and len(m.group(0)) <= 5:
            return m.group(0)
        else:
            return '.jpeg'

    # get the prefix
    def __getPrefix(self, name):
        return name[:name.find('.')]

    # page_number
    # start_page
    def start(self, word, page_number=1,start_page=1):
        self.amount = page_number * 60
        self.__start_amount=(start_page-1)*60
        self.__getImages(word)


crawler = Crawler(0.05)
crawler.start(word, 1,2)
#crawler.start('农场', 3,3)
#crawler.start('ozawa', 5)
