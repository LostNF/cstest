#!/usr/bin/env python
# encoding: utf-8

import urllib
import urllib2
import re
import os

class Csgo(object):

    def __init__(self):
        self.siteurl = 'http://www.igxe.cn/search?search_page_no='

    def getpage(self,pagenum,no,gunname):
        url = self.siteurl + str(pagenum) + '&search_relate_price=&search_product' \
                                            '_type_id=' + str(no) + '&search_categor' \
                                            'y_id=4&search_sort_key=0&search_sort_rul' \
                                            'e=1&search_is_sticker=0&search_' \
                                            'key=' + str(gunname) + '&search_price_gt' \
                                            'e=&search_price_lte=&search_rarity_id=&s' \
                                            'earch_exterior_id=&search_is_stattrak=0&' \
                                            'search_type=730'
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8','ignore')
        except urllib2.URLError,e:
            if hasattr(e,"code"):               #判断e是否具有code属性，也就是相关错误号
                print e.code
            if hasattr(e,"reason"):
                print e.reason

    def getcontent(self,pagenum,no,gunname):
        page = self.getpage(pagenum,no,gunname)
        pattern = re.compile('<div.*?class="mod-hotEquipment-hd">.*?href="/(.*?)">.*?style=".*?">(.*?)<.*?<b>(.*?)<.*?com-img">.*?img src="(.*?)".*?span>(.*?)<.*?class="s3">.*?<strong>(.*?)<',re.S)
        items = re.findall(pattern,page)
        guns = []
        for item in items:
            #print item[0],item[1],item[2],item[3],item[4],item[5]
            guns.append([item[0],item[1],item[2],item[3],item[4],item[5]])
            #0:产品编号 1：名称 2：磨损 3：图片 4：磨损度 5：价格
        return guns

    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            return True
        else:
            return False

    def savecontent(self,content,name):
        filename = name + "/" + name + ".txt"
        f = open(filename,"w+")
        print u"正在保存", filename, u"的信息"
        f.write(content.encode('utf-8'))

    def saveimg(self,imageurl,filename):
        u = urllib2.urlopen(imageurl)
        data = u.read()
        f = open(filename,'w+')
        f.write(data)
        print u"正在保存",filename,u"的图片"
        f.close()



    def saveinfo(self,pagenum,no,gunname):
        contents = self.getcontent(pagenum,no,gunname)
        for item in contents:
            # 0:产品编号 1：名称 2：磨损 3：图片 4：磨损度 5：价格
            print u"发现产品",item[0],item[1],u"磨损:",item[2],item[4]
            print u"价格：",item[5]
            imageurl = item[3]
            productname = item[0]
            content = item[1] + item[0] + item[2] + item[4] + item[5]
            self.mkdir(productname)
            self.savecontent(content,productname)
            #self.saveimg(imageurl,productname)


spider = Csgo()
#spider.getcontent(1,27,"火神")
spider.saveinfo(1,27,"火神")




