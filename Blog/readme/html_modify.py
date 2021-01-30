import re
import base64
import os
from   PIL import Image


def html_modify(fileName):
    #读取readme.md文件
    inputFile = open(fileName, 'r')
    line_vec   = inputFile.readlines()
    inputFile.close()
    #----------------------------------------------------------------
    #1. 为页面添加home建，主页不添加
    if (not "index.html" in fileName):
      home_button = "<p><a href='/'><span>Home</span></a></p>"
      for n_line in range( len(line_vec)):
          line    = line_vec[n_line]      
          if ("<body class='typora-export'>" in line):
            break
      line_vec.insert(n_line, home_button)
    
    #----------------------------------------------------------------
    #2.修改title为head1，而不是与文件名相同
    for n_line in range( len(line_vec)):
        line    = line_vec[n_line]      
        h1_name = re.findall(r'<span>(.+?)</span></h1>',line)
        if (len(h1_name) > 0 ):
            h1_name = h1_name[0]
            break
    for n_line in range( len(line_vec)):
        line  = line_vec[n_line]      
        title = re.findall(r'<title>(.+?)</title>',line)
        if (len(title) > 0 ):
            titleStr_old = '<title>%s</title>'%title[0]
            titleStr_new = '<title>%s</title>'%h1_name
            line  = line.replace(titleStr_old, titleStr_new,1);
            #修改line_vec
            line_vec[n_line] = line
            break
    
    #逐行判断是否需要修改
    for n_line in range( len(line_vec)):
        line = line_vec[n_line]      

        #----------------------------------------------------------------
        #3. 删除第5行的连接     
        link_str = "<link href='https://fonts.loli.net/css?family=Open+Sans:400italic,700italic,700,400&subset=latin,latin-ext' rel='stylesheet' type='text/css' />"
        if (link_str in line): line=line.replace(link_str, "",1);
        
        #----------------------------------------------------------------
        #4. 修改根目录
        link_str = 'http://www.yxkblog.com'
        if (link_str in line): line=line.replace(link_str, ""); #全部删除

        #----------------------------------------------------------------
        #5. 修改其中的图片格式
        output = re.findall(r'<img src=(.+?) />',line)
        for figure_str in output:
            #找到图片文件名和缩放尺寸
            figure_name = re.findall(r'"(.+?)" style',figure_str)
            zoom_ratio  = re.findall(r'zoom:(.+?)%;',figure_str)
            
            #判断是否找到正确的文件名和缩放尺寸
            if (len(figure_name) != 1 or len(zoom_ratio) != 1 ): continue
            #如果上面运行正确，则进行下面修改图片格式的代码    
                    
            #----------------------------------------------------------------
            #a. 修改缩放格式
            im         = Image.open(figure_name[0]) #返回一个Image对象
            zoom_ratio = float(zoom_ratio[0])
            #得到缩放后的width &height
            width  = im.size[0]
            height = im.size[1]
            width  = width  * zoom_ratio/100
            height = height * zoom_ratio/100     
            #修改缩放格式
            zoomStr_old   = 'style'+re.findall(r'" style(.+?)%;',figure_str)[0]+'%;"'
            zoomStr_new   = 'width="%.2f" height="%.2f"'%(width,height)
            figureStr_new = figure_str.replace(zoomStr_old,zoomStr_new,1)
            
            #----------------------------------------------------------------
            #b. 将图片src改为base64的数据，进行封装
            #图片修改为base64的格式
            with open(figure_name[0], 'rb') as f:
               image_base64 = str(base64.b64encode(f.read()))[2:]
            src_new       = "'data:img/png;base64, " + image_base64
            src_old       = '"' + figure_name[0] + '"'
            figureStr_new = figureStr_new.replace(src_old, src_new,1)
            
            #----------------------------------------------------------------
            #c. 将前面的修改写进line数据中
            line=line.replace(figure_str, figureStr_new, 1)
            
        #修改line_vec
        line_vec[n_line] = line

    ##----------------------------------------------------------------
    ##将修改后的数据返回readme.md
    outputFile = open(fileName, 'w')
    for line in line_vec:
        outputFile.write(line)
    outputFile.close()

#---------------------------------------------------------------------
if __name__ == "__main__":  
    files = os.listdir('.')
    for fileName in files:
        if('.html' in fileName):
            html_modify(fileName)
