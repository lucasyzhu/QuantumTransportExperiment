#----------------------------------------------------------------
#读取readme.md文件
readmeFile = open('readme.md', 'r')
line_vec   = readmeFile.readlines()
readmeFile.close()

#----------------------------------------------------------------
#修改其中的图片格式
for n_line in range( len(line_vec)):
    line = line_vec[n_line]
    
    #print(line[-1])
    #开头添加 <div align=center>
    if ('<img ' in line): 
        if ('center' in line): continue
        else:
            line = '<div align=center>'+ line
    #末尾添加</div>
    if ('/>' in line):
        if ('</div>' in line): continue
        else:
            line = line.replace('\n','') + '</div>'+'\n'
    #修改图片缩放格式
    if ('style="zoom:' in line):
        pos_start = line.index('style="zoom')
        pos_end   = line.index('%;"')+3
        style_str = line[pos_start:pos_end]
        zoom_ratio= float(style_str[12:-3])
        #line.replace(style_str, 'width="%.1f%'%zoom_ratio)
        line=line.replace(style_str, 'width="%.1f'%zoom_ratio+'%"')
    #修改line_vec
    line_vec[n_line] = line

#----------------------------------------------------------------
#将修改后的数据返回readme.md
readmeFile = open('readme.md', 'w')
for line in line_vec:
    readmeFile.write(line)
readmeFile.close()
        
