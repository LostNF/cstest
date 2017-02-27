#-*- coding:utf-8 -*-

import urllib
import urllib2
import re


class Csgo(object):
    
    def __init__(self):
        self.siteurl = 'http://www.igxe.cn/search?search_page_no='

    def getpage(self,pagenum,no,gunname):
        url = self.siteurl + str(pagenum) + '&search_relate_price=&search_product_type_id=' + str(no) + '&search_category_id=4&search_sort_key=0&search_sort_rule=1&search_is_sticker=0&search_key=' + str(gunname) + '&search_price_gte=&search_price_lte=&search_rarity_id=&search_exterior_id=&search_is_stattrak=0&search_type=730'
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason

    def getcontent(self,pagenum,no,gunname):
        page = self.getcontent(pagenum,no,gunname)
        pattern = re.compile('<div.*?class="mod-hotEquipment-hd">.*?href="(.*?)">.'
                             '*?style=".*?">(.*?)<.*?<b>(.*?)<.*?com-img">.*?img src'
                             '="(.*?)".*?span>(.*?)<.*?class="s3">.*?<strong>(.*?)<'
                             ,re.S)
        items = re.findall(pattern,page)
        for item in items:


    def getimg(self,imageurl,filename):
        u = urllib2.urlopen(imageurl)
        data = u.read()
        f = open(filename,'wb')
        f.write(data)
        f.close()

     def savecontent(self,content,name):
         filename = name + "/" + name + ".txt"


    
