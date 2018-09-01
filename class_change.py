# -*- coding=utf-8 -*- 
import os
import pdb

import re
import sys
#reload(sys)
#sys.setdefaultencoding("utf8")
 
def translate(test):
    re_words = re.compile(u"[\u4e00-\u9fa5]+")
    m =  re_words.search(test,0)
    print (m)
    #print (m.group())
    #outStr = ''.join(result)
    outStr = re.findall(re_words, test ) # 查询出所有的匹配字符串
    #pdb.set_trace()###########
    return outStr


def cgclass():
    #pdb.set_trace()##########
    dic = {'扎洞':'1','毛斑':'2','擦洞':"3",'毛洞':"4",\
            '织稀':"5",'吊经':"6",'缺经':"7",'跳花':"8",'油渍':"9",'污渍':"9",
            '边扎洞':'1','吊纬':"6",'缺纬':"7",'经跳花':"8"}
    #pdb.set_trace()##########
    for key in dic:
        #pdb.set_trace()###########
        str1 = key
        newstr = 'defect_'+dic[key]
        ##被替换的文件名
        #filename="filename"
        ##获取指定字符串的行号
        #os.system('export filename = '+ path + file)
        #pdb.set_trace()############
        #os.system('line=`sed -n \'/'+str1+'/=\' \''+path+file+'\'`')
        ##删除这行
        #os.system('sed -i "$line d" \''+path+file+'\'')
        ##在删除的行插入新字符串
        #os.system('sed -i "$line i'+'\'       <name>'+newstr+'</name>'+'\'" \''+path+file+'\'')
        #pdb.set_trace()############
        os.system('sed -i \'/>'+key+'</s/>'+key+'</>defect_'+dic[key]+'</g\' *.xml')


def main(path):
    for root, dirs, files in os.walk(path):
        #os.path.join(dirpath, dirnames)
        print(root)
        #print(dirs)
        files.sort()
        print(files)
        #os.system('cd '+path)
        pdb.set_trace()
        for file in files:              
            with open(path+file, "r+") as f:
                    lines = f.readlines()
                    for line in lines:
                        outStr = translate(line)
                        if outStr != None:
                            for Str in outStr:
                                os.system('sed -i \'/'+Str+'/s/'+Str+'/defect_10/g\' \''+path+file+'\'')

path = './rrt_bu_label/'
#cgclass()
main(path)