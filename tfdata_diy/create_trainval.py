#generate trainval.txt,Match the file name with the number of categories.
#keep the xmls folder clean ,just store xml file.
#函数目标：将xml文件夹的所有文件，按照顺序，写在标记的一个txt文件夹里，并且增加每个xml中，标记对象的数目
import os
import re
import xml.etree.ElementTree as ET

#open all files in xmls ,and get files' name
#打开xmls文件夹所有的文件名字，不包括后缀
dirs=[x.split('.')[0] for x in os.listdir('xmls')]
#print(dirs)
#创建一个空列表
li = []

for d in dirs:
  match = re.match(r'([a-zA-Z_]+)([0-9]+)',d,re.I).groups()
# match split the name with letter and digital without File extension.
# d是单个的文件名字，没有后缀，然后将名字中的数字和字母分开，数字分开是为了后面的排序，防止读取文件出现乱序
#  print("match",match)
  
#  下面是打开这个xml文件，查找有几个object。
#  filename是文件路径和名称。root获取根节点
#  root.findall可以查找文件中的某个节点，返回值是[<Element 'object' at 0x0000017EEE964A48>, 
#  <Element 'object' at 0x0000017EEE964908>, 
#  <Element 'object' at 0x0000017EEE964598>]
#  需要len()一下就可以了
  filename = "xmls/" + d + ".xml"
#  print("filename",filename)
  root = ET.parse(filename).getroot()
#  object = root.getchildren()  
#  print("object",root.findall('object'))
  object_num = len(root.findall('object'))
#  print("object_num",object_num)
#  最后将这三个值分别加到li列表中。
  
  li.append([match[0],match[1],object_num])
  
#根据文件名数字进行排序
sorted_li = sorted(li,key=lambda li:int(li[1]))
  
#
#  filename = 'xmls\'+
#  tree = ET.ElementTree(file='doc1.xml')
#将li列表写进txt文件
with open('trainval.txt','w') as f:
  for x in sorted_li:
    f.write(x[0]+x[1]+' '+str(x[2])+'\n')


